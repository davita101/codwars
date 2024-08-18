class Human {
  constructor(name) {
    this.name = name
  }
}

class Woman extends Human {
  constructor(name = "Adam") {
    super(name)
  }
}
class Man extends Human {
  constructor(name = "Adam") {
    super(name)
  }
}

class God {
  static create() {
    return [new Man(), new Woman()]
  }
}

