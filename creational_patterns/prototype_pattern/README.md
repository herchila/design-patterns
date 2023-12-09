The Prototype Pattern is a creational design pattern used to create duplicate objects while keeping performance in mind. It involves copying existing objects without the overhead of reinitializing them from scratch. A real-world use case for the Prototype Pattern is in a graphic design application where users can duplicate shapes or objects.

In a graphic design application, users often need to create multiple instances of similar shapes or objects with slight variations. Using the Prototype Pattern, you can allow users to clone existing objects and then modify them, which is more efficient than creating each shape from scratch, especially if the object initialization is resource-intensive.

Take a look [this implementation](./shape_prototype.py):

* `ShapePrototype` is the prototype class with a `clone` method that uses Python's `copy.deepcopy` to create a deep copy of the object.
* `PrototypeRegistry` is a class that manages a registry of prototypes. It allows registering and unregistering prototypes and cloning them with optional modifications.
* The client code creates a registry, registers a circle prototype, and then clones it while modifying its properties.

The Prototype Pattern in this scenario provides a flexible and efficient way to duplicate and customize shapes. This is particularly useful in applications where object creation is complex or resource-intensive, as it avoids the overhead of new initialization and leverages the efficiency of cloning existing objects.
