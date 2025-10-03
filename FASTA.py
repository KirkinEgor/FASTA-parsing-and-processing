class Seq:
    """
    Represents a biological sequence (DNA, RNA, or protein) with metadata.
    
    This class stores sequence data along with its identifier tag and provides
    basic bioinformatics properties such as sequence length and alphabet type
    detection.
    
    Attributes:
        tag (str): Sequence identifier or description (text after '>' in FASTA)
        sequence (str): The biological sequence string
    """


    def __init__(self, tag: str, sequence: str):
        """
        Initialize a Seq object with tag and sequence.
        
        Args:
            tag: Sequence identifier or description line
            sequence: Biological sequence string (DNA, RNA, or protein)

        Raises:
            ValueError: Wrong data format
        """
        
        if not isinstance(tag, str) or not isinstance(sequence, str):
            raise ValueError("Wrong data format")
        

        self.tag = tag
        self.sequence = sequence
    

    def __str__(self) -> str:
        """
        Return sequence in FASTA format.
        
        Returns:
            String representation in FASTA format with '>' prefix for tag
        """
        

        return f""">{self.tag}
{self.sequence}"""
    

    @property
    def seq_len(self) -> int:
        """
        Get the length of the biological sequence.
        
        Returns:
            Integer length of the sequence
        """


        return len(self.sequence)
    

    @property
    def alphabet(self) -> str:
        """
        Detect the type of biological sequence based on its characters.
        
        Determines if the sequence is nucleotide (only A, C, T, G) or protein
        (contains other amino acid characters).
        
        Returns:
            'Nucleotide' if sequence contains only A, C, T, G characters,
            'Protein' otherwise
        """


        if set(self.sequence) == {"A", "C", "T", "G"}:
            return "Nucleotide"
        else:
            return "Protein"
    

class FastaReader:
    """
    A FASTA file reader that parses biological sequences from FASTA format files.

    It yields Seq objects containing sequence tags and sequences.
    
    Attributes:
        inp_path (str): Path to the input FASTA file. Can be None for interactive input.
    """


    def __init__(self, inp_path: str = None):
        """
        Initialize the FastaReader with an optional file path.
        
        Args:
            inp_path: Path to the FASTA file. If None, user will be prompted
                     to enter the path when read_seq() is called. Defaults to None
        """


        self.inp_path = inp_path
        

    def read_seq(self):
        """
        Read and parse sequences from the FASTA file.
        
        This method is a generator that yields Seq objects one at a time.
        If no file path was provided during initialization, it will prompt
        the user to enter a file path interactively.
        
        Yields:
            Seq: Sequence objects containing tag and sequence data
            
        Raises:
            FileNotFoundError: If the specified FASTA file cannot be found
            ValueError: Empty sequence is found
                        Empty tag is found
        """


        if self.inp_path is None:
            self.inp_path = input("Enter the path to the FASTA-file")
        seq = ""
        tag = None
        with open(self.inp_path) as file:
            for line in file:
                if not line:
                    continue
                line = line.strip()
                if line.startswith(">"):
                    if tag is not None:
                        if not seq:
                            raise ValueError("Empty sequence is found")
                        yield Seq(tag, seq)
                        seq = ""
                    tag = line[1:]
                    if not tag:
                        raise ValueError("Empty tag is found")
                else:
                    seq += line
            if tag is not None:
                if not seq:
                    raise ValueError("Empty sequence is found")
                yield Seq(tag, seq)