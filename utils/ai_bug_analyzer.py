def analyze_error(error_message):
    if "NoSuchElementException" in error_message:
        return (
            "Possible cause: The test failed because Selenium could not find an element on the page.\n"
            "Suggested next step: Check if the locator is correct, if the element exists, or if an explicit wait is needed."
        )

    if "AssertionError" in error_message:
        return (
            "Possible cause: The actual result did not match the expected result.\n"
            "Suggested next step: Check the expected value, current page URL, and application behavior."
        )

    if "TimeoutException" in error_message:
        return (
            "Possible cause: The page or element took too long to load.\n"
            "Suggested next step: Add an explicit wait or check application performance."
        )

    return (
        "Possible cause: Unknown failure type.\n"
        "Suggested next step: Review the error message, screenshot, and browser state."
    )