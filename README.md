# Quiz #2: Identify self-"un"invoked methods.

Your submission must satisfy the following requirements:

* R1. Shall initialize your assignment repository from 
* R2. Write your `invoke_analyzer.py` in the repository.
* R3. Test your `invoke_analyzer.py` by using `pytest`.
* R4. You need to let your TA know your repository URL and your student ID together via Slack.
* R5. Check out `test_analyzer1.py` to figure out the output format.
* R6. Assume that there are "NO" nested classes/methods and anonymous classes.
* R7. Assume that there are nested directories in the input path.
* R8. The function `collect_uninvoked_methods(...)` takes a path of a directory containing multiple Python source code files, and produces a map of classes. The keys of the map are classes, and the values are a set of methods that are never invoked by their own classes. If there is no uninvoked method, the value should be an empty set (`{}`).
* R9. The returned value of the above function should include **ONLY** classes defined in the Python files.


## Note:

* N1. `pytest` (based on `test_analyzer1.py`) is just for validating your program. The final grading will be made by other test cases.
* N2. Submissions via GitHub Classroom will only be accepted. Submissions via LMS or any other means are not accepted.
* N3. DO NOT change files in this repository except for `invoke_analyzer.py`. Adding new files are allowed.
* N4. Late submissions after 2:45pm are *NOT* allowed.

