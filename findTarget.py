from Bio import SeqIO
import os
import os.path
import sys
import shutil
import pathlib
import subprocess
import argparse


def split_gbk(path, tmp_dir):
    with open(path) as file:
        container = []
        index = 1
        for line in file:
            if line.startswith('//'):
                container.append(line)
                with open(tmp_dir + '/tmp.{}.gb'.format(index), 'w') as tmp:
                    for line in container:
                        tmp.write(line)
                tmp.close()
                container = []
                index += 1
            else:
                container.append(line)
    return(0)


def write_fasta(data, path):
    with open(path, 'a') as file:
        for record in data:
            file.write('>{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\n'.format(record['locus'],
                                                               record['start'],
                                                               record['end'],
                                                               record['strand'],
                                                               record['product'],
                                                               record['protein_id'],
                                                               record['locus_tag']))
            file.write(record['seq'] + '\n\n')
    return(0)


# def parse_gbk(tmp_dir, file):
#     container = []
#     data = SeqIO.read("{0}/{1}".format(tmp_dir, file), "genbank")
#     cds = [f for f in data.features if f.type == "CDS"]
#     for i in cds:
#         try:
#             record = {}
#             record['seq'] = i.qualifiers['translation'][0]
#             record['locus'] = data.id
#             record['locus_tag'] = i.qualifiers['locus_tag'][0]
#             record['product'] = i.qualifiers['product'][0]
#             record['protein_id']= i.qualifiers['protein_id'][0]
#             record['start'] = int(i.location.start)
#             record['end'] = int(i.location.end)
#             record['strand'] = i.location.strand
#             container.append(record)
#         except:
#             print('problem with {}'.format(i.qualifiers['locus_tag'][0]) )
#     return(container)



def parse_gbk(tmp_dir, file):
    container = []
    data = SeqIO.read("{0}/{1}".format(tmp_dir, file), "genbank")
    cds = [f for f in data.features if f.type == "CDS"]
    for i in cds:
        if 'translation' in i.qualifiers:
            record = {}
            record['seq'] = i.qualifiers['translation'][0]
            record['locus'] = data.id
            if 'locus_tag' in i.qualifiers:
                record['locus_tag'] = i.qualifiers['locus_tag'][0]
            else:
                record['locus_tag'] = 'None'
            record['product'] = i.qualifiers['product'][0]
            record['protein_id']= i.qualifiers['protein_id'][0]
            record['start'] = int(i.location.start)
            record['end'] = int(i.location.end)
            record['strand'] = i.location.strand
            container.append(record)
    return(container)



def run_hhmer(model_path, fasta_path, results_path):
    args = ["hmmsearch", '{}'.format(model_path), '{}'.format(fasta_path)]
    r = subprocess.run(args, capture_output=True)
    args = ["hmmsearch", '{}'.format(model_path), '{}'.format(fasta_path)]
    r = subprocess.run(args, capture_output=True)
    with open(results_path, 'wb') as file:
        file.write(r.stdout)
    file.close()
    return(r.stdout)


def gbk_to_fasta(gbk_path, fasta_path, tmp_dir):
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    split_gbk(gbk_path, tmp_dir)
    files = [i for i in os.listdir(tmp_dir) if not i.startswith('.')]
    for file in files:
        data = parse_gbk(tmp_dir, file)
        write_fasta(data, fasta_path)
    shutil.rmtree(tmp_dir)
    return(0)

    
# def main():
#     wd = "/Users/tsukanov/Downloads/"
#     gbs = [i for i in os.listdir(wd) if ".gb" in i]
#     models = ['phi29-1-191', 'phi29-192-229', 'phi29-398-420', 'phag-polymerase-b']
#     models_dir = '/Users/tsukanov/Documents/Хакатон/'
#     tmp_dir = wd + "/tmp/"
#     for g in gbs:
#         print(g)
#         gbk_path = wd + g
#         name = g.split('.')[0]
#         fasta_path = wd + "/{0}.fasta".format(name)
#         if os.path.isfile(fasta_path):
#             os.remove(fasta_path)
#         gbk_to_fasta(gbk_path, fasta_path, tmp_dir)
#         for model in models:
#             model_path = models_dir + "/{0}.hmm".format(model)
#             results_path = wd + "/hmmer_{0}_res_{1}.txt".format(name, model)
#             run_hhmer(model_path, fasta_path, results_path)
#     return(0)



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('genebank', action='store', help='path to GeneBank file')
    parser.add_argument('fasta', action='store', help='path to write Fasta (parsed CDS from GeneBank file)')
    parser.add_argument('results', action='store', help='dir to write results')
    parser.add_argument('tag', action='store', help='tag for output files')
    parser.add_argument('-t', '--tmp', action='store', dest='tmp_dir',
                        required=False, default='./tmp', help='tmp dir')
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    return(parser.parse_args())


def main():
    args = parse_args()
    gbk_path = args.genebank
    fasta_path = args.fasta
    results_dir = args.results
    tag = args.tag
    tmp_dir = args.tmp_dir
    this_dir, this_filename = os.path.split(__file__)
    models_dir = os.path.join(this_dir, 'models')
    models = ['phi29-1-191', 'phi29-192-229', 'phi29-398-420', 'phage-polymerase-b']
    if os.path.isfile(fasta_path):
        os.remove(fasta_path)
    gbk_to_fasta(gbk_path, fasta_path, tmp_dir)
    for model in models:
        model_path = models_dir + "/{0}.hmm".format(model)
        results_path = results_dir + "/hmmer_{0}_res_{1}.txt".format(tag, model)
        run_hhmer(model_path, fasta_path, results_path)
    return(0)


if __name__=="__main__":
    main()