# Rencana Kerja Penelitian

## Optimasi Pipeline ASR untuk Komputasi CPU Rendah-Sumber Daya

---

# 1. Pendahuluan dan Spesifikasi Target Sistem

Penelitian ini bertujuan untuk merancang, mengimplementasikan, dan menguji secara empiris sebuah pipeline transkripsi wicara (_Automatic Speech Recognition_ / ASR) berkinerja tinggi yang dioptimalkan khusus untuk arsitektur CPU _commodity_ tanpa kartu grafis terdedikasi (_non-CUDA_).

Sistem dikembangkan di atas proyek AIRA (_Automated Interview Recruitment Assistant_) dengan mengintegrasikan algoritma deteksi aktivitas suara Silero VAD sebagai penyaring keheningan sebelum audio didekode oleh model transformator terdistilasi Distil-Whisper-Small (`distil-small.en`, 166 juta parameter) dalam format graf ONNX Runtime terkuantisasi dinamis 8-bit (INT8).

---

## 1.1 Batasan Perangkat Keras Pengujian

Seluruh eksperimen, pengolahan data, kompilasi graf model, dan pengujian performa dilakukan secara luring (_offline-first_) pada spesifikasi fisik berikut:

| Komponen  | Spesifikasi                                                                                |
| --------- | ------------------------------------------------------------------------------------------ |
| Processor | AMD Ryzen 5 5500U (6 Cores, 12 Threads, base clock 2.10 GHz, AVX2 instruction set enabled) |
| Memory    | 16 GB DDR4 RAM                                                                             |
| Graphics  | Integrated AMD Radeon Graphics (~497 MB VRAM)                                              |
| Storage   | Solid-State Drive (SSD) dengan sisa ruang penyimpanan ≈ 165 GB                             |

---

## 1.2 Target Metrik Performa Sistem

Akselerasi pipeline yang diusulkan ditargetkan memenuhi kriteria batas fungsional berikut.

### Akurasi Transkripsi

Penurunan akurasi semantik minimal dengan nilai _Word Error Rate_ (WER) di bawah selisih 4% dibandingkan model dasar FP32.

\[
\text{WER} = \frac{S + D + I}{N}
\]

Keterangan:

- \(S\) = jumlah substitusi kata
- \(D\) = jumlah penghapusan kata
- \(I\) = jumlah penyisipan kata
- \(N\) = jumlah total kata pada transkrip acuan (_ground-truth_)

---

### Kecepatan Pemrosesan

Nilai _Real-Time Factor_ (RTF) ditargetkan ≤ 0.3, yang berarti kecepatan transkripsi minimal 3× lebih cepat dibanding durasi audio asli secara luring pada CPU.

\[
\text{RTF} = \frac{T*{\text{inference}}}{T*{\text{audio}}}
\]

Keterangan:

- \(T\_{\text{inference}}\) = durasi eksekusi inferensi model
- \(T\_{\text{audio}}\) = durasi total audio input

---

### Konsumsi Memori

- Ukuran file model < 200 MB
- Konsumsi RAM runtime aktif < 1 GB

---

# 2. Jadwal dan Pipeline Pengerjaan Penelitian (12 Minggu)

```text
[M1-M3] Fase 1: Setup Environment, Dataset RecruitView, Preprocessing
   │
[M4-M6] Fase 2: Integrasi Silero VAD, Konversi ONNX, Kuantisasi INT8
   │
[M7-M9] Fase 3: Benchmarking (WER, RTF, CPU/RAM), Integrasi AIRA & Gemini API
   │
[M10-M12] Fase 4: Analisis Kurva Pareto, Penyusunan Skripsi & Draft Paper SINTA/IEEE
```
