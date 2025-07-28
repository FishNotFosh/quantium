from task_4 import app


def test_header(dash):
    dash.start_server(app)
    dash.wait_for_element("#header", timeout=20)


def test_visualization(dash):
    dash.start_server(app)
    dash.wait_for_element("#visualization", timeout=20)


def test_region_picker(dash):
    dash.start_server(app)
    dash.wait_for_element("#region_picker", timeout=20)
