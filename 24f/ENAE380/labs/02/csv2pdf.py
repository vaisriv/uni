import pandas as pd 
import pdfkit

CSV = pd.read_csv("SortingTests.csv")
CSV.to_html("SortingTests.html")

pdfkit.from_url("SortingTests.html", "SortingTests.pdf")
