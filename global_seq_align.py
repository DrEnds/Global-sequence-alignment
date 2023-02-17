from Bio import pairwise2
from Bio.pairwise2 import format_alignment
import matplotlib.pyplot as plt
import streamlit as st
import webbrowser

st.set_page_config(page_title='Seq Align', page_icon="🧬", layout="wide")

#page header
st.header("Global sequence alignment using the Needleman-Wunsch algorithm")

st.markdown("---")

st.markdown("`According to Wikipedia`")
st.write("The Needleman-Wunsch method is a bioinformatics tool used to align protein or nucleotide sequences. That was one of the first times dynamic programming was used to compare biological sequences. Saul B. Needleman and Christian D. Wunsch created the algorithm, which was published in 1970. The method breaks a major problem into smaller problems, and then uses the answers to the smaller problems to discover an optimal solution to the larger problem. It is also known as the optimum matching algorithm and the global alignment approach. The Needleman-Wunsch method is still commonly employed for optimum global alignment, especially where global alignment quality is critical. The method assigns a score to each potential alignment, and its goal is to identify all possible alignments with the highest score.")
url = 'https://en.wikipedia.org/wiki/Needleman%E2%80%93Wunsch_algorithm#:~:text=The%20Needleman%E2%80%93Wunsch%20algorithm%20is,Needleman%20and%20Christian%20D.'
if st.button('Learn more from Wikipedia'):
    webbrowser.open_new_tab(url)

st.markdown("---")

#defining a function
def seq_align_run(a,b):

    alignments = pairwise2.align.globalxx(a, b)
    alignment = alignments[0]   
    alignment_str = format_alignment(*alignment)

    # Create a plot of the alignment using Matplotlib
    fig, ax = plt.subplots()
    ax.text(0.01, 0.8, alignment_str, transform=ax.transAxes, fontsize=7, verticalalignment='top')

    # Set the plot's title and axis labels
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    #ax.spines['left'].set_visible(False)
    ax.set_title("Sequence Alignment")

    # Hide the axis ticks and show the plot
    plt.xticks([])
    plt.yticks([])
    st.pyplot(fig)




# Define the sequences to align
seq1 = st.text_area("Sequence 1")
seq2 = st.text_area("Sequence 2")


#button to show results
if st.button('Run Analysis'):
    seq_align_run(seq1, seq2)
    



st.markdown("*By DrEnds*")
