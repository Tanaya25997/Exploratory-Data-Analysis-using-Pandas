import subprocess


def process(script_name):
    output = subprocess.run(['python',script_name], capture_output=True, text=True)
    if output.returncode != 0:
        print(f"Error running {script_name}: {output.stderr}")
    else:
        print(f"Successfully ran {script_name}")
        print(output.stdout)

    




def run_pandas():

    process('pandas_dataCSV.py')





if __name__ == '__main__':

    run_pandas()
    
    
    


