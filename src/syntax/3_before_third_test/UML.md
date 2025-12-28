# IT-2 UML Notes

## 1. Class Diagram

Class diagrams show the **structured parts of a system**.

### 1.1 Class

- Represents objects with **attributes** and **methods**.
- Notation:
  +----------------+
  | ClassName |
  +----------------+
  | attribute1 |
  | attribute2 |
  +----------------+
  | method1() |
  | method2() |
  +----------------+

### 1.2 Objects

- Instance of a class.
- Notation:
  objectName : ClassName

### 1.3 Connections (Relationships)

| Type                         | Notation  | Description                        |
| ---------------------------- | --------- | ---------------------------------- |
| Association                  | ───────── | General connection between classes |
| Aggregation                  | ◇──────── | Whole-part relationship (weak)     |
| Composition                  | ◆──────── | Whole-part relationship (strong)   |
| Inheritance / Generalization | ──▷       | One class inherits from another    |
| Dependency                   | ---->     | One class depends on another       |

### 1.4 Multiplicities (Numbers)

- Indicates how many objects can participate in a connection.
- Examples:
  - `1` : exactly one
  - `0..1` : zero or one
  - `*` : many
  - `1..*` : one or more

**Example with multiplicity:**
ClassA 1 ── \* ClassB

This means **one instance of ClassA can have many instances of ClassB**.

---

## 2. Additional Notes

- Keep diagrams **simple and clear**.
- Use **multiplicities** to show how many objects participate in relationships.
- Combine **class diagrams with use case and sequence diagrams** for full system understand
