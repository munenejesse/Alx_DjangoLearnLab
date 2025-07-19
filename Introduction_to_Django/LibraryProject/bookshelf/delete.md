
---

### File: `LibraryProject/bookshelf/delete.md`

```markdown
# Delete Operation

```python
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
print(books)  # Output: <QuerySet []>
