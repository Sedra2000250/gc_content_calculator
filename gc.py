def calculate_gc_content(sequence):
    sequence = sequence.upper()
    g = sequence.count('G')
    c = sequence.count('C')
    gc_content = (g + c) / len(sequence) * 100
    return round(gc_content, 2)

# مثال
dna = "ATGCGCGTA"
gc = calculate_gc_content(dna)
print(f"GC Content: {gc}%")
