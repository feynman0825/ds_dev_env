from demo_package.demo_module.module import demo_func


def test_demo_function():
    # Given
    expected_result = "demo function with 100"

    # When
    actual_result = demo_func(100)

    # Then
    assert isinstance(actual_result, str)
    assert actual_result == expected_result
