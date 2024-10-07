import streamlit as st
import requests

from utils.logging_config import setup_logging

setup_logging()

st.set_page_config(page_title="Report", page_icon="📈")

st.markdown("# Report")
st.sidebar.header("Report")


response = requests.get("http://backend:8000/templates")
templates = response.json().get("templates", [])

selected_template = st.sidebar.radio("Select Template", templates, index=0)
selected_menu = st.sidebar.radio("Select Menu", ["Edit Template", "Edit Variables", "Capture Screenshots", "Render"], index=0)

# tabs =  st.tabs(templates)
# template_tabs = dict(zip(templates, tabs))
# for (tpl, tab) in template_tabs.items():

tpl = selected_template

if selected_menu == "Edit Template":
    if st.button("Edit Template", key=f"edit_template_{tpl}"):
        container_edit = st.container(border=True, key=f"container_edit_{tpl}")
        response = requests.get(f"http://backend:8000/template/{tpl}")
        template_content = response.json().get("content", "")
        new_content = container_edit.text_area("Template Content", template_content, height=300, key=f"content_{tpl}")
        if container_edit.button("Save Template", key=f"save_{tpl}"):
            response = requests.post(f"http://backend:8000/template/{tpl}", json={"content": new_content})
            container_edit.success("Template saved successfully")

if selected_menu == "Edit Variables":
    # if st.button("Edit Variables", key=f"edit_variables_{tpl}"):
    if True:
        def render_json_input(st, json_data, parent_key=''):
            if isinstance(json_data, dict):
                for key, value in json_data.items():
                    new_key = f"{parent_key}.{key}" if parent_key else key
                    if isinstance(value, (dict, list)):
                        st.text(new_key)
                        render_json_input(st, value, new_key)
                    else:
                        json_data[key] = st.text_input(new_key, value=str(value))
            elif isinstance(json_data, list):
                sub_container = st.container(border=True)
                sub_tabs = sub_container.tabs([ json_data[i]["name"] for i in range(len(json_data))])
                for i, item in enumerate(json_data):
                    new_key = f"{parent_key}[{i}]"
                    sub_tabs[i].text(new_key)
                    render_json_input(sub_tabs[i], item, new_key)

        response = requests.get(f"http://backend:8000/template/{tpl}/context")
        context_json = response.json().get("context", {})
        container_var = st.container(border=True, key=f"container_variables_{tpl}")

        selected_category = st.sidebar.radio("Select Category",
                                                   [None] + list(context_json.keys()),
                                                   index=None)
        if selected_category is None:
            container_var.text("Select a category to edit variables")

        for e in context_json:
            if e != selected_category:
                continue
            if isinstance(context_json[e], dict):
                container_var.subheader(e)
                render_json_input(container_var, context_json[e], e)
            elif isinstance(context_json[e], list):
                container_var.subheader(e)
                render_json_input(container_var, context_json[e], e)
            else:
                context_json[e] = container_var.text_input(e, context_json[e])

        if container_var.button("Save Variables", key=f"save_variables_{tpl}"):
            response = requests.post(f"http://backend:8000/template/{tpl}/context", json=context_json)
            if response.status_code == 200:
                container_var.success("Variables saved successfully")
            else:
                container_var.error("Error saving variables")

if selected_menu == "Capture Screenshots":
    if st.button("Capture Screenshots", key=f"screenshot_{tpl}"):
        st.text("Screenshot")
        screenshot_container = st.container(border=True)
        response = requests.post(f"http://backend:8000/template/{tpl}/screenshots")
        screenshots = response.json().get("screenshots", [])
        for screenshot in screenshots:
            screenshot_container.json(screenshot)

if selected_menu == "Render":
    if st.button("Render", key=f"render_{tpl}"):
        response = requests.post(f"http://backend:8000/template/{tpl}/render")
        if response.status_code == 200:
            st.html(response.json().get("content"))
        else:
            st.error("Error rendering template")

