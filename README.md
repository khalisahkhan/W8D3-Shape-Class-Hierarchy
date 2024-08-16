# W8D3-Shape-Class-Hierarchy

# Overview
This project demonstrates a class hierarchy for representing different geometric shapes using Object-Oriented Programming (OOP) principles. The hierarchy includes a base class Shape and derived classes for specific shapes: Circle, Rectangle, and Triangle. Each class handles shape-specific calculations for area and perimeter while inheriting common attributes and methods from the base class.

Shape Base Class: Defines a common interface for all shapes and handles color management.
Methods: calculate_area(), calculate_perimeter(), get_color(), set_color()

Rectangle Class: Computes area and perimeter for rectangles.
Methods: calculate_area(), calculate_perimeter()

Triangle Class: Computes area (using Heron's formula) and perimeter for triangles.
Methods: calculate_area() (using Heron's formula), calculate_perimeter()

Circle Class: Computes area and perimeter for circles.
Methods: calculate_area(), calculate_perimeter()
Polymorphism: Demonstrates using a list of shapes to perform calculations and display details.

# Clone repository
git clone

# Requirements
Python 3

# Run Code
python shape_hierarchy.py
