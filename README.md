# Python Simple In-Memory Function Cache

This example demonstrates a basic in-memory caching mechanism in Python. It simulates an 'expensive' operation that takes time, then shows how caching its result significantly speeds up subsequent calls for the same data, reducing server load and improving response times. The first call for a given key will be slow (cache miss), while subsequent calls for the same key will be fast (cache hit).

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal using a Python interpreter:
`python main.py`

## Original Article

This example accompanies the Turkish article: [Sistem Tasarımında Caching: Yüksek Performansın Sırrı](https://fatihsoysal.com/blog/sistem-tasariminda-caching-yuksek-performansin-sirri/).

## License

MIT — see [LICENSE](LICENSE).
