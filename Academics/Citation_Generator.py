
# New MLA generator with variances
#There is also a citation counter for simple copy/pasting in one's bibliography.


def MLA_citation_generator():
    citation_counter = 0

    while True:

        citation_counter += 1

        authors = input("Authors (Separate multiple authors with a comma): ").split(",")
        formatted_authors = ""

        if len(authors) >= 3:
            formatted_authors = authors[0].strip().split()[1] + " et al."
        elif len(authors) == 2:
            last_names = [author.strip().split()[1] for author in authors]  # Extract last names
            formatted_authors = ", ".join(last_names)
        else:
            name_parts = authors[0].strip().split()
            formatted_authors = f"{name_parts[1]}, {name_parts[0]}."  # Last Name, First Name
        
        title = input("Title of the Source: ")
        container = input("Title of the Container (Book, Journal, etc.): ")
        version = input("Version (if applicable): ")
        edition = input("Edition (if applicable): ")
        series = input("Series (if applicable): ")
        publisher = input("Publisher: ")
        publication_date = input("Publication Date: ")
        location = input("Location (Page numbers, URL, etc.):")

        citation_parts = [
            formatted_authors,
            f"\"{title}\"" if title else "",
            container,
            version,
            edition,
            series,
            publisher,
            publication_date,
            location
        ]
        
        mla_citation = ", ".join(part for part in citation_parts if part)
        mla_citation += "."  # Add period at the end
        print(f"{citation_counter}. {mla_citation}")

        create_another = input("Create another citation? (y/n): ")
        if create_another.lower() != "y":
            break

MLA_citation_generator()

# APA Citation Generator

def APA_citation_generator():
    citation_counter = 0

    while True:

        citation_counter += 1

        authors = input("Authors (Separate multiple authors with a comma): ").split(",")
        formatted_authors = ""

        if len(authors) >= 2:
            formatted_authors_list = []
            for author in authors:
                name_parts = author.strip().split()
                last_name = name_parts[-1]
                first_initial = name_parts[0][0]
                formatted_authors_list.append(f"{last_name}, {first_initial}.")
            formatted_authors = ", ".join(formatted_authors_list)
        else:
            name_parts = authors[0].strip().split()
            last_name = name_parts[-1]
            first_initial = name_parts[0][0]
            formatted_authors = f"{last_name}, {first_initial}."
        
        title = input("Title of the Source: ")
        container = input("Title of the Container (e.g., Book, Journal, etc.): ")
        edition = input("Edition (if applicable): ")
        volume = input("Volume (if applicable): ")
        issue = input("Issue (if applicable): ")
        page_numbers = input("Page numbers: ")
        doi = input("DOI (if applicable): ")
        publication_date = input("Publication Date: ")

        citation_parts = [
            formatted_authors,
            f"({publication_date})." if publication_date else "",
            title,
            container,
            f"({edition})" if edition else "",
            f"({volume})" if volume else "",
            f"({issue})" if issue else "",
            page_numbers,
            doi
        ]

        apa_citation = " ".join(part for part in citation_parts if part)
        apa_citation += "."
        print(f"{citation_counter}. {apa_citation}")

        create_another = input("Create another citation? (y/n): ")
        if create_another.lower() != "y":
            break

APA_citation_generator()
