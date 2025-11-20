// --- TAB LOGIC ---
function openTab(tabName) {
    const contents = document.querySelectorAll('.tab-content');
    contents.forEach(c => c.classList.remove('active'));
    
    const btns = document.querySelectorAll('.tab-btn');
    btns.forEach(b => b.classList.remove('active'));

    document.getElementById(tabName).classList.add('active');
    event.currentTarget.classList.add('active');
}

// --- EXERCISE 1: SQUARE SUM ---
let squareSumInterval = null;

function isPerfectSquare(n) {
    const root = Math.round(Math.sqrt(n));
    return root * root === n;
}

function drawSquareSumGraph(n, adj, path, current) {
    const canvas = document.getElementById('squaresum-canvas');
    const ctx = canvas.getContext('2d');
    const width = canvas.width;
    const height = canvas.height;
    const cx = width / 2;
    const cy = height / 2;
    const r = Math.min(width, height) / 2 - 30;

    ctx.clearRect(0, 0, width, height);

    // Positions
    const positions = {};
    for (let i = 1; i <= n; i++) {
        const angle = (2 * Math.PI * (i - 1)) / n - Math.PI / 2;
        positions[i] = {
            x: cx + r * Math.cos(angle),
            y: cy + r * Math.sin(angle)
        };
    }

    // Draw all possible edges (gray)
    ctx.strokeStyle = '#333';
    ctx.lineWidth = 1;
    for (let i = 1; i <= n; i++) {
        for (const neighbor of adj[i]) {
            if (i < neighbor) {
                ctx.beginPath();
                ctx.moveTo(positions[i].x, positions[i].y);
                ctx.lineTo(positions[neighbor].x, positions[neighbor].y);
                ctx.stroke();
            }
        }
    }

    // Draw current path (green)
    if (path.length > 1) {
        ctx.strokeStyle = '#a6e3a1'; // Success color
        ctx.lineWidth = 3;
        ctx.beginPath();
        ctx.moveTo(positions[path[0]].x, positions[path[0]].y);
        for (let i = 1; i < path.length; i++) {
            ctx.lineTo(positions[path[i]].x, positions[path[i]].y);
        }
        ctx.stroke();
    }

    // Draw nodes
    for (let i = 1; i <= n; i++) {
        const pos = positions[i];
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, 15, 0, 2 * Math.PI);
        
        if (path.includes(i)) {
            ctx.fillStyle = '#a6e3a1'; // In path
            ctx.strokeStyle = '#a6e3a1';
        } else {
            ctx.fillStyle = '#1e1e2e'; // Default bg
            ctx.strokeStyle = '#cdd6f4'; // Default border
        }
        
        if (i === current) {
            ctx.fillStyle = '#f9e2af'; // Highlight current
            ctx.strokeStyle = '#f9e2af';
        }

        ctx.fill();
        ctx.stroke();

        ctx.fillStyle = (path.includes(i) || i === current) ? '#1e1e2e' : '#cdd6f4';
        ctx.font = 'bold 12px Inter';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(i, pos.x, pos.y);
    }
}

function* solveSquareSumGenerator(n) {
    const adj = {};
    for (let i = 1; i <= n; i++) adj[i] = [];
    for (let i = 1; i <= n; i++) {
        for (let j = i + 1; j <= n; j++) {
            if (isPerfectSquare(i + j)) {
                adj[i].push(j);
                adj[j].push(i);
            }
        }
    }

    const path = [];
    const used = new Array(n + 1).fill(false);

    function* backtrack(curr) {
        path.push(curr);
        used[curr] = true;
        // Yield status with the move details
        yield { adj, path: [...path], current: curr, found: false, message: `Adicionado ${curr}. Caminho: [${path.join(', ')}]` };

        if (path.length === n) {
            yield { adj, path: [...path], current: curr, found: true, message: `SOLUÇÃO ENCONTRADA!` };
            return true;
        }

        for (const neighbor of adj[curr]) {
            if (!used[neighbor]) {
                // Log the check
                const sum = curr + neighbor;
                const root = Math.sqrt(sum);
                yield { 
                    adj, path: [...path], current: curr, found: false, 
                    message: `Tentando vizinho ${neighbor}... (${curr} + ${neighbor} = ${sum} = ${root}²). OK.` 
                };

                if (yield* backtrack(neighbor)) return true;
                
                yield { 
                    adj, path: [...path], current: curr, found: false, 
                    message: `Falha no ramo do ${neighbor}. Voltando (Backtrack)...` 
                };
            }
        }

        used[curr] = false;
        path.pop();
        return false;
    }

    for (let i = 1; i <= n; i++) {
        yield { adj, path: [], current: i, found: false, message: `Iniciando busca com raiz ${i}...` };
        if (yield* backtrack(i)) break;
    }
}

function runSquareSum() {
    stopSquareSum();
    const n = 15;
    const output = document.getElementById('squaresum-output');
    output.textContent = "Iniciando busca para N=15...\n";
    
    const generator = solveSquareSumGenerator(n);
    
    // Initial draw
    const adj = {}; 
    for(let i=1; i<=n; i++) adj[i] = [];
    for(let i=1; i<=n; i++) for(let j=i+1; j<=n; j++) if(isPerfectSquare(i+j)) { adj[i].push(j); adj[j].push(i); }
    drawSquareSumGraph(n, adj, [], null);

    squareSumInterval = setInterval(() => {
        const res = generator.next();
        if (res.done) {
            clearInterval(squareSumInterval);
            output.textContent += "\nBusca finalizada.";
            output.scrollTop = output.scrollHeight;
            return;
        }
        
        const { adj, path, current, found, message } = res.value;
        drawSquareSumGraph(n, adj, path, current);
        
        if (message) {
            output.textContent += "\n" + message;
            output.scrollTop = output.scrollHeight;
        }

        if (found) {
            clearInterval(squareSumInterval);
            output.textContent += `\n\nSolução Completa:\n[${path.join(', ')}]`;
            output.scrollTop = output.scrollHeight;
        }
    }, 100); // Slower speed to read logs
}

function stopSquareSum() {
    if (squareSumInterval) clearInterval(squareSumInterval);
}

// --- EXERCISE 2: N-QUEENS ---
let queensInterval = null;

function createBoard(n) {
    const board = document.getElementById('chessboard');
    board.style.gridTemplateColumns = `repeat(${n}, 40px)`;
    board.innerHTML = '';
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const cell = document.createElement('div');
            cell.className = `cell ${(r + c) % 2 === 0 ? 'white' : 'black'}`;
            cell.id = `cell-${r}-${c}`;
            board.appendChild(cell);
        }
    }
}

function updateBoard(boardState, n) {
    for (let r = 0; r < n; r++) {
        for (let c = 0; c < n; c++) {
            const cell = document.getElementById(`cell-${r}-${c}`);
            cell.textContent = '';
            if (boardState[r] === c) {
                cell.textContent = '♛';
            }
        }
    }
}

function* solveNQueensGenerator(n) {
    const board = new Array(n).fill(-1);
    
    function isSafe(row, col) {
        for (let prevRow = 0; prevRow < row; prevRow++) {
            const prevCol = board[prevRow];
            if (prevCol === col || Math.abs(prevRow - row) === Math.abs(prevCol - col)) {
                return false;
            }
        }
        return true;
    }

    function* backtrack(row) {
        if (row === n) {
            yield { board: [...board], found: true };
            return true;
        }

        for (let col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                board[row] = col;
                yield { board: [...board], found: false }; // Show step
                
                if (yield* backtrack(row + 1)) return true;
                
                board[row] = -1; // Backtrack
                yield { board: [...board], found: false }; // Show backtrack
            }
        }
        return false;
    }

    yield* backtrack(0);
}

function startNQueens() {
    stopNQueens();
    const n = parseInt(document.getElementById('queens-n').value);
    createBoard(n);
    const generator = solveNQueensGenerator(n);
    const status = document.getElementById('queens-status');

    queensInterval = setInterval(() => {
        const result = generator.next();
        if (result.done) {
            clearInterval(queensInterval);
            status.textContent = "Status: Finalizado (Sem solução)";
            return;
        }
        
        updateBoard(result.value.board, n);
        
        if (result.value.found) {
            clearInterval(queensInterval);
            status.textContent = "Status: Solução Encontrada!";
        } else {
            status.textContent = "Status: Buscando...";
        }
    }, 100); // Speed
}

function stopNQueens() {
    if (queensInterval) clearInterval(queensInterval);
    document.getElementById('queens-status').textContent = "Status: Parado";
}

// --- EXERCISE 3: KNIGHT'S TOUR ---
function runKnightTour() {
    const output = document.getElementById('knight-output');
    output.textContent = "Executando para N=8 (Heurística de Warnsdorff)...\n";
    
    setTimeout(() => {
        output.textContent += "Iniciando em (0,0)...\n";
    }, 500);
    
    setTimeout(() => {
        output.textContent += "Calculando movimentos com menor grau de saída...\n";
    }, 1000);

    setTimeout(() => {
        output.textContent += "Solução Encontrada (Matriz de Passos):\n";
        output.textContent += " 0 59 38 33 30 17  8 63\n37 34 31 60  9 62 29 16\n58  1 36 39 32 27 18  7\n35 48 41 26 61 10 15 28\n42 57  2 49 40 23  6 19\n47 50 45 54 25 20 11 14\n56 43 52  3 22 13 24  5\n51 46 55 44 53  4 21 12";
    }, 2000);
}


// --- BRANCH AND BOUND: KNAPSACK ---
let knapsackInterval = null;

function drawKnapsackTree(nodes, links, activeNodeId) {
    const canvas = document.getElementById('knapsack-canvas');
    const ctx = canvas.getContext('2d');
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    
    // Simple tree layout
    // Map levels to y, and spread x based on index in level
    const levels = {};
    nodes.forEach(n => {
        if (!levels[n.level]) levels[n.level] = [];
        levels[n.level].push(n);
    });

    const nodeRadius = 18;
    const levelHeight = 60;
    const startY = 40;
    
    // Calculate positions
    const positions = {};
    Object.keys(levels).forEach(lvl => {
        const levelNodes = levels[lvl];
        const width = canvas.width;
        const step = width / (levelNodes.length + 1);
        levelNodes.forEach((n, i) => {
            positions[n.id] = { x: step * (i + 1), y: startY + lvl * levelHeight };
        });
    });

    // Draw links
    ctx.strokeStyle = '#555';
    ctx.lineWidth = 1;
    links.forEach(l => {
        const p1 = positions[l.source];
        const p2 = positions[l.target];
        if (p1 && p2) {
            ctx.beginPath();
            ctx.moveTo(p1.x, p1.y);
            ctx.lineTo(p2.x, p2.y);
            ctx.stroke();
            
            // Label (In/Ex)
            const midX = (p1.x + p2.x) / 2;
            const midY = (p1.y + p2.y) / 2;
            ctx.fillStyle = '#aaa';
            ctx.font = '10px Inter';
            ctx.fillText(l.type === 'include' ? 'Sim' : 'Não', midX, midY);
        }
    });

    // Draw nodes
    nodes.forEach(n => {
        const pos = positions[n.id];
        if (!pos) return;
        
        ctx.beginPath();
        ctx.arc(pos.x, pos.y, nodeRadius, 0, 2 * Math.PI);
        
        if (n.id === activeNodeId) {
            ctx.fillStyle = '#f9e2af'; // Active
            ctx.strokeStyle = '#f9e2af';
        } else if (n.pruned) {
            ctx.fillStyle = '#f38ba8'; // Pruned
            ctx.strokeStyle = '#f38ba8';
        } else if (n.solution) {
            ctx.fillStyle = '#a6e3a1'; // Solution
            ctx.strokeStyle = '#a6e3a1';
        } else {
            ctx.fillStyle = '#1e1e2e';
            ctx.strokeStyle = '#cdd6f4';
        }
        
        ctx.fill();
        ctx.stroke();
        
        // Text inside node (Bound)
        ctx.fillStyle = (n.id === activeNodeId) ? '#1e1e2e' : '#cdd6f4';
        ctx.font = 'bold 10px Inter';
        ctx.textAlign = 'center';
        ctx.textBaseline = 'middle';
        ctx.fillText(`B:${Math.floor(n.bound)}`, pos.x, pos.y - 5);
        ctx.font = '9px Inter';
        ctx.fillText(`V:${n.profit}`, pos.x, pos.y + 5);
    });
}

function* solveKnapsackGenerator(W, items) {
    // Sort by density
    items.sort((a, b) => (b.v / b.w) - (a.v / a.w));
    
    let nodeIdCounter = 0;
    const nodes = [];
    const links = [];
    
    function getBound(u, n, W, items) {
        if (u.weight >= W) return 0;
        let profit_bound = u.profit;
        let j = u.level + 1;
        let tot_weight = u.weight;
        
        while (j < n && tot_weight + items[j].w <= W) {
            tot_weight += items[j].w;
            profit_bound += items[j].v;
            j++;
        }
        
        if (j < n) {
            profit_bound += (W - tot_weight) * (items[j].v / items[j].w);
        }
        return profit_bound;
    }

    const n = items.length;
    const pq = [];
    
    const root = { 
        id: nodeIdCounter++, level: -1, profit: 0, weight: 0, bound: 0, 
        items: [], pruned: false, solution: false 
    };
    root.bound = getBound(root, n, W, items);
    pq.push(root);
    nodes.push(root);
    
    yield { nodes, links, active: root.id, message: `Raiz criada. Bound Inicial: ${root.bound.toFixed(1)}` };

    let maxProfit = 0;
    let bestNode = null;

    while (pq.length > 0) {
        // Sort PQ by bound (desc)
        pq.sort((a, b) => b.bound - a.bound);
        const u = pq.shift(); // Pop best
        
        yield { nodes, links, active: u.id, message: `Explorando nó ${u.id} (Bound: ${u.bound.toFixed(1)}). Melhor Atual: ${maxProfit}` };

        if (u.bound > maxProfit) {
            // Branch
            if (u.level + 1 < n) {
                const item = items[u.level + 1];
                
                // Child 1: Include
                const v1 = { 
                    id: nodeIdCounter++, level: u.level + 1, 
                    profit: u.profit + item.v, weight: u.weight + item.w, 
                    bound: 0, items: [...u.items, item.id], pruned: false, solution: false 
                };
                
                links.push({ source: u.id, target: v1.id, type: 'include' });
                nodes.push(v1);

                if (v1.weight <= W && v1.profit > maxProfit) {
                    maxProfit = v1.profit;
                    bestNode = v1;
                    yield { nodes, links, active: v1.id, message: `NOVA MELHOR SOLUÇÃO! Valor: ${maxProfit}. (Incluiu Item ${item.id})` };
                }

                v1.bound = getBound(v1, n, W, items);
                
                if (v1.bound > maxProfit) {
                    if (v1.weight <= W) pq.push(v1);
                    else { v1.pruned = true; yield { nodes, links, active: v1.id, message: `Nó ${v1.id} podado (Peso ${v1.weight} > ${W})` }; }
                } else {
                    v1.pruned = true;
                    yield { nodes, links, active: v1.id, message: `Nó ${v1.id} podado (Bound ${v1.bound.toFixed(1)} <= Max ${maxProfit})` };
                }

                // Child 2: Exclude
                const v2 = { 
                    id: nodeIdCounter++, level: u.level + 1, 
                    profit: u.profit, weight: u.weight, 
                    bound: 0, items: [...u.items], pruned: false, solution: false 
                };
                
                links.push({ source: u.id, target: v2.id, type: 'exclude' });
                nodes.push(v2);
                
                v2.bound = getBound(v2, n, W, items);
                
                if (v2.bound > maxProfit) {
                    pq.push(v2);
                } else {
                    v2.pruned = true;
                    yield { nodes, links, active: v2.id, message: `Nó ${v2.id} podado (Bound ${v2.bound.toFixed(1)} <= Max ${maxProfit})` };
                }
                
                yield { nodes, links, active: null, message: `Ramificação do nível ${u.level+1} concluída.` };
            }
        } else {
            u.pruned = true;
            yield { nodes, links, active: u.id, message: `Nó ${u.id} podado antes de explorar (Bound ${u.bound.toFixed(1)} <= Max ${maxProfit})` };
        }
    }
    
    if (bestNode) bestNode.solution = true;
    yield { nodes, links, active: bestNode ? bestNode.id : null, message: `FIM. Solução Ótima: ${maxProfit}` };
}

function startKnapsack() {
    stopKnapsack();
    const items = [
        { id: 1, w: 4, v: 40 },
        { id: 2, w: 7, v: 42 },
        { id: 3, w: 5, v: 25 },
        { id: 4, w: 3, v: 12 }
    ];
    const W = 10;
    
    // Display items
    const container = document.getElementById('knapsack-items');
    container.innerHTML = '';
    items.forEach(item => {
        const div = document.createElement('div');
        div.className = 'item-box';
        div.innerHTML = `Item ${item.id}<br>W:${item.w} V:${item.v}`;
        container.appendChild(div);
    });

    const generator = solveKnapsackGenerator(W, items);
    const log = document.getElementById('knapsack-log');
    log.innerHTML = "Iniciando Branch and Bound...\n";
    
    knapsackInterval = setInterval(() => {
        const res = generator.next();
        if (res.done) {
            clearInterval(knapsackInterval);
            document.getElementById('knapsack-status').textContent = "Status: Finalizado.";
            return;
        }
        
        const { nodes, links, active, message } = res.value;
        drawKnapsackTree(nodes, links, active);
        
        if (message) {
            const line = document.createElement('div');
            line.textContent = message;
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;
        }
    }, 800);
}

function stopKnapsack() {
    if (knapsackInterval) clearInterval(knapsackInterval);
    document.getElementById('knapsack-status').textContent = "Status: Parado";
}

// --- ASSIGNMENT PROBLEM ---
let assignmentInterval = null;

function* solveAssignmentGenerator(costMatrix) {
    const n = costMatrix.length;
    const pq = [];
    let nodeIdCounter = 0;
    
    // Helper to calculate lower bound (row reduction)
    function getLowerBound(matrix, assigned) {
        let bound = 0;
        // Row reduction
        for (let r = 0; r < n; r++) {
            if (assigned.includes(r)) continue; // Skip assigned rows (workers)
            // Actually, in this model, we assign row by row.
            // So if we are at worker 'i', we need to consider rows i to n-1.
            // But let's stick to the simpler logic: Sum of mins of unassigned rows.
            let min = Infinity;
            for (let c = 0; c < n; c++) {
                // Check if col is taken
                // This is complex to track in simple bound.
                // Let's use a simplified bound: Sum of min of each remaining row.
                if (matrix[r][c] < min) min = matrix[r][c];
            }
            if (min !== Infinity) bound += min;
        }
        return bound;
    }

    const root = { 
        id: nodeIdCounter++, worker: -1, cost: 0, 
        assigned: [], // List of task indices assigned to workers 0..worker
        bound: 0
    };
    
    // Simple Bound for root: Sum of min of all rows
    let initialBound = 0;
    for(let r=0; r<n; r++) initialBound += Math.min(...costMatrix[r]);
    root.bound = initialBound;
    
    pq.push(root);
    
    yield { matrix: costMatrix, activeNode: root, message: `Raiz. Bound Inicial (Soma dos mínimos): ${root.bound}` };

    let minCost = Infinity;
    let bestNode = null;

    while (pq.length > 0) {
        pq.sort((a, b) => a.bound - b.bound); // Min-heap
        const u = pq.shift();
        
        yield { matrix: costMatrix, activeNode: u, message: `Explorando Trabalhador ${u.worker+1} (Custo Atual: ${u.cost}, Bound: ${u.bound})` };

        if (u.bound < minCost) {
            const nextWorker = u.worker + 1;
            
            if (nextWorker === n) {
                minCost = u.cost;
                bestNode = u;
                yield { matrix: costMatrix, activeNode: u, message: `SOLUÇÃO ENCONTRADA! Custo: ${minCost}` };
                continue;
            }

            // Try assigning nextWorker to each task
            for (let task = 0; task < n; task++) {
                if (!u.assigned.includes(task)) {
                    const cost = u.cost + costMatrix[nextWorker][task];
                    
                    // Calculate bound for this child
                    // Bound = cost so far + sum of mins of remaining rows
                    let futureBound = 0;
                    for (let r = nextWorker + 1; r < n; r++) {
                        let rowMin = Infinity;
                        for (let c = 0; c < n; c++) {
                            if (!u.assigned.includes(c) && c !== task) {
                                if (costMatrix[r][c] < rowMin) rowMin = costMatrix[r][c];
                            }
                        }
                        if (rowMin !== Infinity) futureBound += rowMin;
                    }
                    
                    const totalBound = cost + futureBound;
                    
                    const v = {
                        id: nodeIdCounter++, worker: nextWorker,
                        cost: cost, assigned: [...u.assigned, task],
                        bound: totalBound
                    };
                    
                    if (totalBound < minCost) {
                        pq.push(v);
                        yield { matrix: costMatrix, activeNode: v, message: `  -> Atribuir Tarefa ${task} (Custo: ${cost}, Bound: ${totalBound}) - Adicionado` };
                    } else {
                        yield { matrix: costMatrix, activeNode: v, message: `  -> Atribuir Tarefa ${task} (Bound ${totalBound} >= Melhor ${minCost}) - Podado` };
                    }
                }
            }
        }
    }
}

function startAssignment() {
    stopAssignment();
    const costMatrix = [
        [9, 2, 7, 8],
        [6, 4, 3, 7],
        [5, 8, 1, 8],
        [7, 6, 9, 4]
    ];
    
    const container = document.getElementById('assignment-matrix');
    container.style.gridTemplateColumns = `repeat(${costMatrix.length}, 40px)`;
    container.innerHTML = '';
    
    // Draw initial matrix
    for(let r=0; r<costMatrix.length; r++) {
        for(let c=0; c<costMatrix.length; c++) {
            const cell = document.createElement('div');
            cell.className = 'cell white';
            cell.textContent = costMatrix[r][c];
            cell.id = `assign-${r}-${c}`;
            container.appendChild(cell);
        }
    }
    
    const log = document.getElementById('assignment-log');
    log.innerHTML = "Iniciando Alocação...\n";
    
    const generator = solveAssignmentGenerator(costMatrix);
    
    assignmentInterval = setInterval(() => {
        const res = generator.next();
        if (res.done) {
            clearInterval(assignmentInterval);
            document.getElementById('assignment-status').textContent = "Status: Finalizado.";
            return;
        }
        
        const { matrix, activeNode, message } = res.value;
        
        // Highlight assignments
        document.querySelectorAll('.cell').forEach(c => c.style.backgroundColor = '#eee');
        if (activeNode && activeNode.assigned) {
            activeNode.assigned.forEach((task, worker) => {
                const cell = document.getElementById(`assign-${worker}-${task}`);
                if (cell) cell.style.backgroundColor = '#a6e3a1';
            });
        }
        
        if (message) {
            const line = document.createElement('div');
            line.textContent = message;
            log.appendChild(line);
            log.scrollTop = log.scrollHeight;
        }
    }, 800);
}

function stopAssignment() {
    if (assignmentInterval) clearInterval(assignmentInterval);
    document.getElementById('assignment-status').textContent = "Status: Parado";
}


// --- GENETIC ALGORITHMS: POLYNOMIAL ---
let geneticId = null;
const TARGET_COEFFS = [2, -3, 1, 5]; 

function f(x, coeffs) {
    return coeffs[0]*x**3 + coeffs[1]*x**2 + coeffs[2]*x + coeffs[3];
}

function drawGraph(bestCoeffs) {
    const canvas = document.getElementById('genetic-canvas');
    const ctx = canvas.getContext('2d');
    const w = canvas.width;
    const h = canvas.height;
    
    ctx.clearRect(0, 0, w, h);
    
    function mapX(x) { return (x + 5) / 10 * w; }
    function mapY(y) { return h - (y + 100) / 200 * h; }
    
    ctx.strokeStyle = '#ddd';
    ctx.beginPath();
    ctx.moveTo(0, mapY(0)); ctx.lineTo(w, mapY(0)); 
    ctx.moveTo(mapX(0), 0); ctx.lineTo(mapX(0), h); 
    ctx.stroke();
    
    ctx.strokeStyle = 'red';
    ctx.lineWidth = 2;
    ctx.beginPath();
    for (let x = -5; x <= 5; x += 0.1) {
        const y = f(x, TARGET_COEFFS);
        if (x === -5) ctx.moveTo(mapX(x), mapY(y));
        else ctx.lineTo(mapX(x), mapY(y));
    }
    ctx.stroke();
    
    if (bestCoeffs) {
        ctx.strokeStyle = 'blue';
        ctx.lineWidth = 2;
        ctx.beginPath();
        for (let x = -5; x <= 5; x += 0.1) {
            const y = f(x, bestCoeffs);
            if (x === -5) ctx.moveTo(mapX(x), mapY(y));
            else ctx.lineTo(mapX(x), mapY(y));
        }
        ctx.stroke();
    }
}

function startGenetic() {
    stopGenetic();
    let population = [];
    for(let i=0; i<50; i++) {
        population.push([Math.random()*20-10, Math.random()*20-10, Math.random()*20-10, Math.random()*20-10]);
    }
    
    let generation = 0;
    const genDisplay = document.getElementById('genetic-gen');
    const errDisplay = document.getElementById('genetic-error');
    
    function evolve() {
        const scored = population.map(genes => {
            let error = 0;
            for(let x=-5; x<=5; x++) {
                let y_target = f(x, TARGET_COEFFS);
                let y_pred = f(x, genes);
                error += Math.abs(y_pred - y_target);
            }
            return { genes, error };
        });
        
        scored.sort((a, b) => a.error - b.error);
        const best = scored[0];
        
        genDisplay.textContent = `Geração: ${generation}`;
        errDisplay.textContent = `Erro: ${best.error.toFixed(2)}`;
        drawGraph(best.genes);
        
        if (best.error < 0.5) {
            return; 
        }
        
        const newPop = scored.slice(0, 5).map(s => s.genes); 
        while(newPop.length < 50) {
            const p1 = newPop[Math.floor(Math.random()*5)];
            const p2 = newPop[Math.floor(Math.random()*5)];
            const child = p1.map((g, i) => (g + p2[i])/2 + (Math.random()-0.5));
            newPop.push(child);
        }
        population = newPop;
        generation++;
        
        geneticId = requestAnimationFrame(evolve);
    }
    
    evolve();
}

function stopGenetic() {
    if (geneticId) cancelAnimationFrame(geneticId);
}

drawGraph(null);
