
## 🔄 Processing Pipeline

This document describes the step-by-step workflow used to prepare historical texts for sentence segmentation and alignment tasks.

---

### **Processing Steps**

1. 📥 **Collect raw texts**  
   - Formats: `.txt`, `.xml`, `.html`, `.pdf` (converted to plain text)  
   - Source: digital editions, OCR outputs, or manually transcribed files

2. 🧹 **Clean and normalize**  
   - Remove unwanted markup, fix inconsistent spacing or encoding  
   - Standardize structural formatting across files (e.g. paragraph markers, metadata)  
   - ⚠️ This step does **not** involve orthographic normalization: original spelling, punctuation, and diacritics are preserved to reflect source variation

3. ✂️ **Segment manually or heuristically**  
   - Annotators apply language-specific rules for sentence or unit segmentation  
   - Mixed approach: hand segmentation + rule-based assistance

4. 🏷️ **Annotate boundaries**  
   - Use the `£` symbol to mark segment boundaries within the text  
   - This delimiter is used across formats for consistency

5. 📂 **Organize into `pre_split/`**  
   - Files in this folder are segmented, but not split into ML subsets  
   - Available in `.txt` and `.json` formats

6. 🔀 **Partition into `train/`, `dev/`, `test/`**  
   - Files in `split/` contain the same content, distributed for model training  
   - Structure: parallel `.json` and `.txt` files with `£` delimiters

---

🔙 Back to [README](../README.md)
