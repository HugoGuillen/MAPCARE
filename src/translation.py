import subprocess
import ollama
from os import path

modelfile=('FROM %s'+
           '\n'+
           'PARAMETER temperature 0'+
           '\n'+
           'SYSTEM Translate from German to English. '+
           'Input text is from the clinical context. '+
           'Acronyms in the text will be medical/surgical acronyms. '+
           'Include an explanation of the term. Do not include a medical disclaimer since this is a research project. '+
           'Do not include greetings, conclusions, or anything else, just the requested output. '+
           'The output format must be the translation followed by a bar symbol followed by the explanation'
           '\n'+
           'MESSAGE user Diagnostischer Ultraschall des Auges'
           '\n'+
           'MESSAGE assistant Diagnostic Ultrasound of the Eye|Ultrasound imaging to diagnose conditions affecting the eye. '+
           'Also known as ocular ultrasonography, is a non-invasive diagnostic procedure that utilizes high-frequency sound waves '+
           'to create images of the eye\'s internal structures. This imaging technique is particularly useful for evaluating the '+
           'posterior segment of the eye, which includes the vitreous humor, retina, choroid, and optic nerve.'
          )

def create_model(model_id: str = 'gemma2') -> str:
    """Build and register a custom Ollama model for translation."""    
    new_model = 'CHOP_%s_translation'%model_id
    output_model = path.join('data',new_model+'.model')
    with open(output_model,'w') as f:
        f.write(modelfile%model_id)
    try:
        result = subprocess.run(
            ["ollama", "create", new_model , "-f", output_model],
            check=True,
            capture_output=True,
            text=True
        )
        print("Output:", result.stdout)
    except subprocess.CalledProcessError as e:
        print("Error:", e.stderr)
    return new_model


def translate_texts(model: str, texts: list[str]) -> list[str]:
    """Batch translate texts via Ollama chat API."""
    results = []
    for t in texts:
        resp = ollama.chat(model=model, messages=[{'role':'user','content':t}])
        results.append(resp['message']['content'])
    return results
