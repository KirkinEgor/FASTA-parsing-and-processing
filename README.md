# FASTA Parser

A Python module for parsing and working with FASTA format biological sequences (DNA, RNA, and protein sequences).

## Features

- **Seq Class**: Represents biological sequences with metadata and basic bioinformatics properties
- **FastaReader Class**: Efficiently parses FASTA files with generator-based reading
- **Sequence Type Detection**: Automatically detects nucleotide vs protein sequences
- **Error Handling**: Comprehensive validation and error reporting
- **FASTA Format Compliance**: Properly handles standard FASTA file format

## Installation

```bash
# Clone the repository
git clone https://github.com/KirkinEgor/FASTA-parsing-and-processing.git
cd FASTA

# Or simply copy the FASTA.py file to your project directory
```

## Quick Start

```python
from FASTA import FastaReader, Seq

# Read sequences from a FASTA file
reader = FastaReader("sequences.fasta") # insert your fasta-file path
for sequence in reader.read_seq():
    print(f"Tag: {sequence.tag}")
    print(f"Sequence: {sequence.sequence}")
    print(f"Length: {sequence.seq_len}")
    print(f"Type: {sequence.alphabet}")
    print("---")
```

## Classes

### Seq Class

Represents a biological sequence with metadata and analysis capabilities.

#### Creating Sequences

```python
# Create a sequence object
dna_sequence = Seq("gene_1", "ATCGATCG")
protein_sequence = Seq("protein_A", "MKTVL")

print(dna_sequence)
# >gene_1
# ATCGATCG
```

#### Properties

- `tag`: Sequence identifier/description
- `sequence`: The biological sequence string
- `seq_len`: Length of the sequence (property)
- `alphabet`: Detected sequence type - "Nucleotide" or "Protein" (property)

### FastaReader Class

Efficient FASTA file parser that yields Seq objects.

#### Basic Usage

```python
# Specify file path during initialization
reader = FastaReader("my_sequences.fasta")

# Or provide path interactively
reader = FastaReader()  # Will prompt for file path
```

#### Reading Sequences

```python
reader = FastaReader("sequences.fasta")

try:
    for seq_obj in reader.read_seq():
        print(f"Processing: {seq_obj.tag}")
        print(f"Length: {seq_obj.seq_len}")
        print(f"Type: {seq_obj.alphabet}")
        
        # Convert to FASTA format
        fasta_string = str(seq_obj)
        
except FileNotFoundError:
    print("FASTA file not found")
except ValueError as e:
    print(f"Error in FASTA file: {e}")
```

## Examples

### Basic Sequence Analysis

```python
from FASTA import Seq

# Create and analyze sequences
seq1 = Seq("human_insulin", "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAED")

print(f"Tag: {seq1.tag}")
print(f"Length: {seq1.seq_len}")
print(f"Type: {seq1.alphabet}")  # Output: Protein
```

### Batch Processing FASTA Files

```python
from FASTA import FastaReader

def analyze_fasta(file_path):
    """Analyze all sequences in a FASTA file."""
    reader = FastaReader(file_path)
    
    stats = {
        'total_sequences': 0,
        'nucleotide_sequences': 0,
        'protein_sequences': 0,
        'total_length': 0
    }
    
    for seq in reader.read_seq():
        stats['total_sequences'] += 1
        stats['total_length'] += seq.seq_len
        
        if seq.alphabet == 'Nucleotide':
            stats['nucleotide_sequences'] += 1
        else:
            stats['protein_sequences'] += 1
            
    return stats

# Usage
results = analyze_fasta("genome_data.fasta")
print(results)
```

## Error Handling

The module provides comprehensive error handling:

```python
try:
    # Invalid sequence creation
    bad_seq = Seq(123, "ATCG")  # Will raise ValueError
    
    # Reading non-existent file
    reader = FastaReader("nonexistent.fasta")
    for seq in reader.read_seq():
        pass
        
except ValueError as e:
    print(f"Data format error: {e}")
except FileNotFoundError:
    print("File not found")
```

## Requirements

- Python 3.6+
- No external dependencies

## File Format Support

The parser supports standard FASTA format:
- Lines starting with `>` indicate sequence headers
- Sequence data can span multiple lines
- Handles empty lines and whitespace
- Supports both nucleotide and protein sequences

Example FASTA file:
```
>sequence_1
ATCGATCGATCG
>sequence_2
MKTVLPRRVLK
```

## Demo program

The repository includes a comprehensive demonstration program:
```
bash

# Run the demo program with sample data
python Demo.py
```
**Sample dataset included**: The demo uses example Sample.fasta file containing nucleotide sequences

## Complete HTML documentation
Browse the full documentation by opening:
```
text

html documentation/index.html
```

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source. Please include proper attribution when using this code.

## Author

Kirkin Egor - 2025
