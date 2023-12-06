from invoke_analyzer import collect_uninvoked_methods

test_input_path = "./src"

def test_methods_uninvoked():
    expected = { 
                "C": {},
                "A": {"__init__", "func1"},
                "B": {"f1", "f2"}
      }

    result = collect_uninvoked_methods(test_input_path)
    assert expected == result
