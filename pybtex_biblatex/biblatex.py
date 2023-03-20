from __future__ import unicode_literals


from pybtex import textutils
from pybtex.bibtex.utils import split_name_list
from pybtex.database import Entry, Person
from pybtex.database.input.bibtex import DuplicateField, Parser
from pylatexenc.latex2text import LatexNodes2Text


class BibLaTeXParser(Parser):
    def process_entry(self, entry_type, key, fields):
        entry = Entry(entry_type)

        if key is None:
            key = 'unnamed-%i' % self.unnamed_entry_counter
            self.unnamed_entry_counter += 1

        seen_fields = set()
        for field_name, field_value_list in fields:
            if field_name.lower() in seen_fields:
                self.handle_error(DuplicateField(key, field_name))
                continue

            field_value = textutils.normalize_whitespace(self.flatten_value_list(field_value_list))
            if field_name in self.person_fields:
                for name in split_name_list(field_value):
                    entry.add_person(Person(LatexNodes2Text().latex_to_text(name)), field_name)
            else:
                entry.fields[field_name] = LatexNodes2Text().latex_to_text(field_value)
            seen_fields.add(field_name.lower())
        self.data.add_entry(key, entry)

    def flatten_value_list(self, value_list):
        return LatexNodes2Text().latex_to_text(''.join(value_list))
