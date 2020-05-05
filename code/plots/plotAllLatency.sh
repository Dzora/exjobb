#!/bin/bash

(python3 plotLatency.py "Home") &
(python3 plotLatency.py "Login") &
(python3 plotLatency.py "List Products") &
(python3 plotLatency.py "Look at Product") &
(python3 plotLatency.py "Add Product to Cart") &
(python3 plotLatency.py "List Products with different page") &
(python3 plotLatency.py "Add Product 2 to Cart") &
(python3 plotLatency.py "Logout") &
