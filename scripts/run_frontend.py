import os

if __name__ == '__main__':
    if(os.name == 'nt'):
        os.chdir('../.venv/Scripts')
    else:
        os.chdir('../.venv/bin')
    os.system("streamlit run ../../project_root_v01/web-automation-system/frontend/app.py --server.port=8501 --server.address=127.0.0.1")
