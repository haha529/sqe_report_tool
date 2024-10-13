import ast
import os
import argparse

def extract_classes_from_file(file_path):
    """Extract classes, methods, and member variables from a file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            base_classes = [base.id for base in node.bases if isinstance(base, ast.Name)]
            methods = [n.name for n in node.body if isinstance(n, ast.FunctionDef)]

            # Extract member variables (based on Assign nodes in the class)
            attributes = []
            for n in node.body:
                if isinstance(n, ast.Assign):
                    for target in n.targets:
                        if isinstance(target, ast.Attribute) and isinstance(target.value, ast.Name) and target.value.id == 'self':
                            attributes.append(target.attr)

            classes.append({
                'name': node.name,
                'bases': base_classes,
                'methods': methods,
                'attributes': attributes
            })

    return classes

def extract_classes_from_directory(directory):
    """Extract classes from all files in a directory."""
    all_classes = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                classes_in_file = extract_classes_from_file(file_path)
                all_classes.extend(classes_in_file)

    return all_classes

def generate_plantuml(classes):
    """Generate PlantUML diagram from class information."""
    uml_lines = ["@startuml"]

    for class_info in classes:
        # Class declaration
        uml_lines.append(f"class {class_info['name']} {{")

        # Add class member variables
        for attribute in class_info['attributes']:
            uml_lines.append(f"  -{attribute}")

        # Add class methods
        for method in class_info['methods']:
            uml_lines.append(f"  +{method}()")

        uml_lines.append("}")

        # Add inheritance relationships
        for base_class in class_info['bases']:
            uml_lines.append(f"{base_class} <|-- {class_info['name']}")

    uml_lines.append("@enduml")
    return "\n".join(uml_lines)

def save_to_file(content, output_path):
    """Save content to a file."""
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(content)

def main():
    # Parse options with argparse
    parser = argparse.ArgumentParser(description="Extract Python classes and generate PlantUML diagram.")
    parser.add_argument('directory', type=str, help='Directory path to extract classes from')
    parser.add_argument('-o', '--output', type=str, default='output_diagram.puml', help='Output file name (.puml extension)')

    args = parser.parse_args()

    # Extract all classes
    classes = extract_classes_from_directory(args.directory)

    # Convert to PlantUML format
    uml_content = generate_plantuml(classes)

    # Save to file
    save_to_file(uml_content, args.output)

    print(f"Class diagram saved to {args.output}")

if __name__ == "__main__":
    main()