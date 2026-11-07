

<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Sorting Algorithms Visualizer</title>

<style>
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: #101827;
    color: white;
    text-align: center;
}

.container {
    max-width: 800px;
    margin: auto;
    padding: 25px 15px;
}

h1 {
    color: #38bdf8;
}

p {
    color: #cbd5e1;
}

input, select, button {
    padding: 12px;
    margin: 7px;
    border-radius: 8px;
    border: none;
    font-size: 16px;
}

input, select {
    width: 90%;
    max-width: 450px;
}

button {
    background: #38bdf8;
    color: #101827;
    font-weight: bold;
    cursor: pointer;
}

button:hover {
    background: #0ea5e9;
}

#bars {
    height: 300px;
    display: flex;
    align-items: flex-end;
    justify-content: center;
    gap: 5px;
    margin-top: 25px;
}

.bar {
    background: #38bdf8;
    flex: 1;
    max-width: 50px;
    border-radius: 5px 5px 0 0;
    color: white;
    font-size: 12px;
    padding-top: 5px;
}

#result {
    margin-top: 20px;
    color: #4ade80;
    font-size: 18px;
    word-wrap: break-word;
}
</style>
</head>

<body>
<div class="container">

<h1>Sorting Algorithms Visualizer</h1>
<p>Enter numbers and visualize how sorting works!</p>

<input id="numbers" type="text"
placeholder="Enter numbers: 45, 12, 78, 23, 9">

<br>

<select id="algorithm">
<option value="bubble">Bubble Sort</option>
<option value="selection">Selection Sort</option>
<option value="insertion">Insertion Sort</option>
<option value="merge">Merge Sort</option>
<option value="quick">Quick Sort</option>
</select>

<br>

<button onclick="sortNumbers()">Sort Numbers</button>
<button onclick="randomNumbers()">Random Numbers</button>

<div id="bars"></div>
<div id="result"></div>

</div>

<script>
function randomNumbers() {
    let nums = Array.from({length: 10}, () =>
        Math.floor(Math.random() * 100) + 1
    );

    document.getElementById("numbers").value = nums.join(", ");
    showBars(nums);
}

function showBars(nums) {
    let bars = document.getElementById("bars");
    bars.innerHTML = "";

    let max = Math.max(...nums, 1);

    nums.forEach(num => {
        let bar = document.createElement("div");
        bar.className = "bar";
        bar.style.height = (num / max * 250) + "px";
        bar.textContent = num;
        bars.appendChild(bar);
    });
}

function bubbleSort(a) {
    for (let i = 0; i < a.length; i++) {
        for (let j = 0; j < a.length - i - 1; j++) {
            if (a[j] > a[j + 1]) {
                [a[j], a[j + 1]] = [a[j + 1], a[j]];
            }
        }
    }
    return a;
}

function selectionSort(a) {
    for (let i = 0; i < a.length; i++) {
        let min = i;

        for (let j = i + 1; j < a.length; j++) {
            if (a[j] < a[min]) min = j;
        }

        [a[i], a[min]] = [a[min], a[i]];
    }
    return a;
}

function insertionSort(a) {
    for (let i = 1; i < a.length; i++) {
        let key = a[i];
        let j = i - 1;

        while (j >= 0 && a[j] > key) {
            a[j + 1] = a[j];
            j--;
        }

        a[j + 1] = key;
    }
    return a;
}

function mergeSort(a) {
    if (a.length <= 1) return a;

    let mid = Math.floor(a.length / 2);
    let left = mergeSort(a.slice(0, mid));
    let right = mergeSort(a.slice(mid));

    let result = [];

    while (left.length && right.length) {
        result.push(left[0] < right[0] ? left.shift() : right.shift());
    }

    return result.concat(left, right);
}

function quickSort(a) {
    if (a.length <= 1) return a;

    let pivot = a[a.length - 1];
    let left = a.filter((x, i) => x <= pivot && i !== a.length - 1);
    let right = a.filter(x => x > pivot);

    return quickSort(left).concat([pivot], quickSort(right));
}

function sortNumbers() {
    let input = document.getElementById("numbers").value;

    let nums = input.split(/[,\s]+/)
        .filter(x => x !== "")
        .map(Number);

    if (nums.length === 0 || nums.some(x => !Number.isFinite(x))) {
        document.getElementById("result").textContent =
            "Please enter valid numbers!";
        return;
    }

    let algorithm = document.getElementById("algorithm").value;
    let sorted;

    if (algorithm === "bubble") sorted = bubbleSort([...nums]);
    if (algorithm === "selection") sorted = selectionSort([...nums]);
    if (algorithm === "insertion") sorted = insertionSort([...nums]);
    if (algorithm === "merge") sorted = mergeSort([...nums]);
    if (algorithm === "quick") sorted = quickSort([...nums]);

    showBars(sorted);

    document.getElementById("result").textContent =
        "Sorted Result: " + sorted.join(", ");
}
</script>

</body>
</html>
