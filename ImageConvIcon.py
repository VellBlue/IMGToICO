import tkinter as tk
from tkinter import filedialog
from PIL import Image

def select_image():
    global input_image_path
    input_image_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg; *.png")])
    if input_image_path:
        selected_image_label.config(text=f"File selezionato: {input_image_path}")

def select_output_folder():
    global output_folder_path
    output_folder_path = filedialog.askdirectory()
    if output_folder_path:
        selected_output_label.config(text=f"Cartella di destinazione selezionata: {output_folder_path}")

def convert_image():
    if input_image_path and output_folder_path:
        try:
            img = Image.open(input_image_path)
            output_file_name = output_name_entry.get()  # Ottieni il nome inserito dall'utente
            if not output_file_name.endswith('.ico'):
                output_file_name += '.ico'  # Assicura che il nome del file finisca con .ico
            output_icon_path = f"{output_folder_path}/{output_file_name}"
            img.save(output_icon_path, format='ICO', sizes=[(16, 16), (32, 32), (48, 48)])
            status_label.config(text=f"Immagine convertita in {output_icon_path}")
        except Exception as e:
            status_label.config(text=f"Errore durante la conversione: {str(e)}")
    else:
        status_label.config(text="Seleziona l'immagine e la cartella di destinazione prima di convertire.")

# Creazione della finestra principale
root = tk.Tk()
root.title("Convertitore immagini in ICO")

# Modifica delle dimensioni della finestra principale
root.geometry("500x300")  # Imposta le dimensioni della finestra principale

# Etichette con dimensioni più grandi e posizionamento tramite grid
selected_image_label = tk.Label(root, text="Nessun file selezionato", font=("Arial", 14))
selected_image_label.grid(row=0, column=0, padx=10, pady=5)

selected_output_label = tk.Label(root, text="Nessuna cartella di destinazione selezionata", font=("Arial", 14))
selected_output_label.grid(row=2, column=0, padx=10, pady=5)

status_label = tk.Label(root, text="", font=("Arial", 12))
status_label.grid(row=6, column=0, padx=10, pady=5)

# Pulsanti con testo più grande e posizionamento tramite grid
select_image_button = tk.Button(root, text="Seleziona immagine", command=select_image, font=("Arial", 12))
select_image_button.grid(row=1, column=0, padx=10, pady=5)

select_output_button = tk.Button(root, text="Seleziona cartella di destinazione", command=select_output_folder, font=("Arial", 12))
select_output_button.grid(row=3, column=0, padx=10, pady=5)

convert_button = tk.Button(root, text="Converti in ICO", command=convert_image, font=("Arial", 12))
convert_button.grid(row=5, column=0, padx=10, pady=5)

# Creazione di un frame per il campo di input e l'etichetta
entry_frame = tk.Frame(root)
entry_frame.grid(row=4, column=0, padx=10, pady=5)

output_name_label = tk.Label(entry_frame, text="Nome del file ICO (opzionale):", font=("Arial", 14))
output_name_label.grid(row=0, column=0, padx=(10, 0), pady=5)

# Campo di input con testo più grande e posizionamento tramite grid nel frame
output_name_entry = tk.Entry(entry_frame, font=("Arial", 12))
output_name_entry.grid(row=0, column=1, padx=(0, 10), pady=5)

# Avvio dell'applicazione
root.mainloop()
