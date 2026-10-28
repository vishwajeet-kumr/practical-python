class TableFormatter:

    def headings(self, headers):
        """
        It defines the headings of the table or row
        """
        raise NotImplementedError()

    def row(self, rowdata):
        """
        shows the rows and it's data
        """
        raise NotImplementedError()


class TextTableFormatter(TableFormatter):

    def headings(self, headers):
        for h in headers:
            print(f"{h:>10s}", end=" ")
        print()
        print(("-" * 10 + " ") * len(headers))

    def row(self, rowdata):
        for d in rowdata:
            print(f"{d:>10s}", end=" ")
        print()


class CSVTableFormatter(TableFormatter):
    def headings(self, headers):
        print(",".join(headers))

    def row(self, rowdata):
        print(",".join(rowdata))


class HTMLTableFormatter(TableFormatter):
    def headings(self, headers):
        print("<tr>" + "".join(f"<th> {h} </th>" for h in headers) + "</tr>")

    def row(self, rowdata):
        print("<tr>" + "".join(f"<th> {d} </th>" for d in rowdata) + "</tr>")


def create_formatter(fmt):
    # prompt = "Write the format of the Data: 'txt', 'CSV', 'HTML' ?\n"
    fmt = fmt.strip().lower()

    if fmt == "txt":
        return TextTableFormatter()
    elif fmt == "csv":
        return CSVTableFormatter()
    elif fmt == "html":
        return HTMLTableFormatter()
    else:
        raise RuntimeError(f"Unknown Format: {fmt}")
