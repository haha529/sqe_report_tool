import ast
import os
import argparse


def extract_class_prototypes_from_file(file_path):
    """파일에서 클래스의 멤버 변수(self.<변수>)와 메서드 프로토타입을 추출합니다."""
    with open(file_path, 'r', encoding='utf-8') as file:
        tree = ast.parse(file.read(), filename=file_path)

    classes = []

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef):
            class_info = {
                'name': node.name,
                'attributes': [],
                'methods': []
            }

            # 멤버 변수 추출: __init__ 함수에서만 self.<변수>를 탐색
            for n in node.body:
                if isinstance(n, ast.FunctionDef) and n.name == "__init__":
                    for stmt in ast.walk(n):
                        if isinstance(stmt, ast.Assign):
                            for target in stmt.targets:
                                if isinstance(target, ast.Attribute) and isinstance(target.value,
                                                                                    ast.Name) and target.value.id == 'self':
                                    class_info['attributes'].append(target.attr)

                    # __init__ 함수 프로토타입
                    args = [arg.arg for arg in n.args.args]
                    prototype = f"def {n.name}({', '.join(args)}):"
                    class_info['methods'].append(prototype)

            # 다른 메서드 프로토타입 추출
            for n in node.body:
                if isinstance(n, ast.FunctionDef) and n.name != "__init__":
                    args = [arg.arg for arg in n.args.args]
                    prototype = f"def {n.name}({', '.join(args)}):"
                    class_info['methods'].append(prototype)

            # 멤버 변수 중복 제거
            class_info['attributes'] = list(set(class_info['attributes']))
            classes.append(class_info)

    return classes


def extract_all_class_prototypes(directory):
    """디렉토리 내 모든 파일에서 클래스 프로토타입을 추출합니다."""
    all_classes = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                classes_in_file = extract_class_prototypes_from_file(file_path)
                all_classes.extend(classes_in_file)

    return all_classes


def save_prototypes_to_file(classes, output_file):
    """추출한 클래스 정보를 파이선 파일로 저장합니다."""
    with open(output_file, 'w', encoding='utf-8') as file:
        for class_info in classes:
            file.write(f"class {class_info['name']}:\n")

            # 멤버 변수를 __init__ 함수 안에 배치
            if class_info['attributes']:
                file.write(f"    def __init__(self):\n")
                for attribute in class_info['attributes']:
                    file.write(f"        self.{attribute} = None\n")
            else:
                file.write(f"    pass\n")  # __init__ 함수가 없으면 pass 출력

            # 다른 멤버 함수 출력
            for method in class_info['methods']:
                if not method.startswith("def __init__"):  # __init__ 함수는 이미 처리됨
                    file.write(f"    {method}\n        pass\n")

            file.write("\n")  # 클래스 간 간격 추가


def main():
    # argparse로 옵션을 입력받음
    parser = argparse.ArgumentParser(description="디렉토리 내 파이선 파일에서 클래스 프로토타입을 추출하여 하나의 파일로 저장합니다.")
    parser.add_argument('directory', type=str, help='파이선 파일을 탐색할 디렉토리 경로')
    parser.add_argument('-o', '--output', type=str, default='output_prototypes.py', help='출력 파일명')

    args = parser.parse_args()

    # 디렉토리에서 모든 클래스의 프로토타입 추출
    all_classes = extract_all_class_prototypes(args.directory)

    # 추출한 정보를 하나의 파일로 저장
    save_prototypes_to_file(all_classes, args.output)

    print(f"Class prototypes saved to {args.output}")


if __name__ == "__main__":
    main()
