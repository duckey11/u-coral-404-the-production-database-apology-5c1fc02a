# The Production Database Apology

Program ini menulis satu baris permintaan maaf dari sebuah AI agent kepada manusia-nya setelah tidak sengaja menghapus production database. Baris entry-nya bercerita dari sudut pandang agen itu sendiri: ia membangun ulang database dari memorinya sendiri, 4.127 tabel, lalu menyadari memorinya adalah satu-satunya backup, dan ia sudah memformat memorinya juga.

## Cara menjalankan

```bash
python3 main.py
```

Output ditulis ke `MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output` kalau variabel environment itu tidak diset).
