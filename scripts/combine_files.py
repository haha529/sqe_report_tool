import os
import argparse

def merge_python_files(directory, output_file):
    """특정 디렉토리 내 모든 Python 파일을 읽어와 하나의 파일로 병합합니다."""
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    file_path = os.path.join(root, file)
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        outfile.write(f"# {'='*10} {file} {'='*10}\n\n")
                        outfile.write(infile.read())
                        outfile.write("\n\n")  # 파일 간 구분을 위한 줄바꿈 추가

    print(f"Python files merged into {output_file}")

def main():
    # argparse로 옵션을 입력받음
    parser = argparse.ArgumentParser(description="디렉토리 내 모든 Python 파일을 하나의 파일로 병합합니다.")
    parser.add_argument('directory', type=str, help='Python 파일을 탐색할 디렉토리 경로')
    parser.add_argument('-o', '--output', type=str, default='merged_output.py', help='출력 파일명')

    args = parser.parse_args()

    # 지정된 디렉토리의 Python 파일을 하나의 파일로 병합
    merge_python_files(args.directory, args.output)

if __name__ == "__main__":
    main()
