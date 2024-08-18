function isDivisible(...x) {
    return x.filter(i => x[0] % i === 0).length === x.length
}