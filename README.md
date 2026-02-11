# DATA221 – Assignment 2

Each question is in its own file.

- `DATA221_Assignment2_Question1.py`: Reads `sample-file.txt`, cleans tokens (lowercase, strip punctuation, keep tokens with at least 2 alphabetic characters), counts word frequencies, and prints the top 10 words.
- `DATA221_Assignment2_Question2.py`: Builds bigrams from the cleaned tokens in `sample-file.txt`, counts bigram frequencies, and prints the most frequent pairs.
- `DATA221_Assignment2_Question3.py`: Finds near-duplicate lines in `sample-file.txt` after normalizing (lowercase + remove all whitespace and punctuation) and prints the number of duplicate sets plus the first two sets.
- `DATA221_Assignment2_Question4.py`: Filters `student.csv` for high-engagement students (studytime, internet, absences), saves results to `high_engagement.csv`, and prints count + average grade.
- `DATA221_Assignment2_Question5.py`: Groups `student.csv` by `grade_band` (Low/Medium/High), calculates number of students, average absences, and % with internet, then saves the summary table to a CSV.
- `DATA221_Assignment2_Question6.py`: Loads `crime.csv`, creates a `risk` category from `ViolentCrimesPerPop`, and prints average `PctUnemployed` for High-Crime vs LowCrime groups.
- `DATA221_Assignment2_Question7.py`: Scrapes the Data Science Wikipedia page, prints the page title, and prints the first main-content paragraph with at least 50 characters.
- `DATA221_Assignment2_Question8.py`: Extracts valid `<h2>` headings from the Data Science Wikipedia page (excluding References/External links/See also/Notes), removes “[edit]”, and saves them to `headings.txt`.
- `DATA221_Assignment2_Question9.py`: Scrapes the Machine Learning Wikipedia page, extracts the first main-content table with at least 3 data rows, builds headers (from `<th>` or `col1...`), pads missing cells, and saves to `wiki_table.csv`.
- `DATA221_Assignment2_Question10.py`: Defines `find_lines_containing(filename, keyword)` for case-insensitive line search and tests it on `sample-file.txt` using the keyword `lorem` (prints count and first 3 matches).
