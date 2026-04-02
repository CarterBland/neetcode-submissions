class Solution {
    /**
     * @param {string[]} tokens
     * @return {number}
     */
    evalRPN(tokens) {
        const  stack = [];
        const operators = new Map([
            ["+", (a, b) => a + b],
            ["-", (a, b) => a - b],
            ["*", (a, b) => a * b],
            ["/", (a, b) => Math.trunc(a / b)],
        ]);

        for (const token of tokens) {
            if (operators.has(token)) {
                const b = stack.pop();
                const a = stack.pop();
                stack.push(operators.get(token)(a, b));
            } else {
                stack.push(Number(token));
            }
        }

        return stack[0];
    }
}
