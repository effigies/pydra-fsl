import os, pytest
from pathlib import Path
from ..prelude import PRELUDE


@pytest.mark.parametrize("inputs, outputs", [])
def test_PRELUDE(inputs, outputs):
    in_file = Path(os.path.dirname(__file__)) / "data_tests/test.nii.gz"
    if inputs is None:
        inputs = {}
    for key, val in inputs.items():
        try:
            inputs[key] = eval(val)
        except:
            pass
    task = PRELUDE(in_file=in_file, **inputs)
    assert set(task.generated_output_names) == set(
        ["return_code", "stdout", "stderr"] + outputs
    )


@pytest.mark.parametrize("inputs, error", [(None, "AttributeError")])
def test_PRELUDE_exception(inputs, error):
    in_file = Path(os.path.dirname(__file__)) / "data_tests/test.nii.gz"
    if inputs is None:
        inputs = {}
    for key, val in inputs.items():
        try:
            inputs[key] = eval(val)
        except:
            pass
    task = PRELUDE(in_file=in_file, **inputs)
    with pytest.raises(eval(error)):
        task.generated_output_names
