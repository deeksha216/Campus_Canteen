
# Task 6 - Code Review

## Code Reviewed
File: classmate_order.py

Note: This is a sample file created for practice,
not code supplied by an actual classmate.

## Six Code Review Comments

### 1. Unclear Function Names
Functions c(), o(), d(), and pay() do not
clearly describe their purpose.
Suggestion: Use names such as calculate_total()
and can_accept_order().

### 2. Duplicate Code
Functions c() and d() repeat GST calculations.
Suggestion: Create a reusable function for
the shared calculation.

### 3. Magic Numbers
Values 0.05, 300, 0.90, and 40 are hard-coded.
Suggestion: Use named constants for GST,
discount limits, discount rates, and slot capacity.

### 4. Missing Input Validation
Negative prices and invalid order counts are
not checked.
Suggestion: Validate inputs before processing.

### 5. Unnecessary Conditional Logic
Function o() uses if/else to return True or False.
Suggestion: Return the comparison directly.

### 6. Misleading Payment Function
Function pay() always returns True without
checking a payment result.
Suggestion: Return the result from a payment
gateway instead of claiming every payment succeeds.

## Review Summary
The sample code could be improved through
clear naming, reusable functions, input validation,
named constants, and reliable payment handling.
