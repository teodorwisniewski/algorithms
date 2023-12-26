

import pytest
from leetcode.problem_1472_BrowserHistory import BrowserHistory

def test_initialization():
    browser = BrowserHistory("leetcode.com")
    assert browser.current_page() == "leetcode.com"  

def test_visit():
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    assert browser.current_page() == "google.com"

def test_back():
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.back(1)
    assert browser.current_page() == "google.com"

def test_forward():
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.back(1)
    browser.forward(1)
    assert browser.current_page() == "facebook.com"

def test_back_forward_limit():
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.back(5)
    assert browser.current_page() == "leetcode.com"
    browser.forward(5)
    assert browser.current_page() == "facebook.com"

def test_complex_sequence():
    browser = BrowserHistory("leetcode.com")
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.visit("youtube.com")
    assert browser.back(1) == "facebook.com"
    assert browser.back(1) == "google.com"
    assert browser.forward(1) == "facebook.com"
    browser.visit("linkedin.com")
    assert browser.forward(2) == "linkedin.com"
    assert browser.back(2) == "google.com"
    assert browser.back(7) == "leetcode.com"


def test_specific_sequence():
    # Initialize the browser history with "leetcode.com"
    browser = BrowserHistory("leetcode.com")

    # Visit subsequent URLs
    browser.visit("google.com")
    browser.visit("facebook.com")
    browser.visit("youtube.com")

    # Move back in history
    assert browser.back(1) == "facebook.com"
    assert browser.back(1) == "google.com"

    # Move forward in history
    assert browser.forward(1) == "facebook.com"

    # Visit a new URL
    browser.visit("leetcode.com")

    # Attempt to move forward, but should not move as history ahead is cleared
    assert browser.forward(2) == "leetcode.com"

    # Move back in history
    assert browser.back(2) == "google.com"
    
    # Test moving back more steps than available in history
    assert browser.back(7) == "leetcode.com"
