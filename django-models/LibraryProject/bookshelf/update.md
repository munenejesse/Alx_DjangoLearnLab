
---

### File: `LibraryProject/bookshelf/update.md`

```markdown
# Update Operation

```python
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

book = Book.objects.get(pk=book.pk)
print(book.title)
# Output: Nineteen Eighty-Four
