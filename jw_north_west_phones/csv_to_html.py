import pandas as pd


def csv_to_html(csv_file, html_file):
    # Read the CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file)

    # Convert the DataFrame to an HTML table
    html_content = df.to_html(index=False)

    # Write the HTML content to a file
    with open(html_file, "w") as file:
        file.write(html_content)


# Example usage
csv_file = "isabela-pretty.csv"  # Replace with your CSV file path
html_file = "output.html"  # Replace with desired HTML file name
csv_to_html(csv_file, html_file)
