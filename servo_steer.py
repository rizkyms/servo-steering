import pyfirmata
import tkinter as tk

# Konfigurasi Arduino
board = pyfirmata.Arduino('/dev/ttyACM1')  # Ganti 'COM3' dengan port Arduino Anda
servo_pin = board.get_pin('d:9:s')  # Pin digital 9 sebagai servo
center = 90  # Posisi tengah
left = 135   # Posisi kiri
right = 45   # Posisi kanan

# Servo mulai di posisi tengah
servo_pin.write(center)

# Fungsi kontrol servo
def move_left(event=None):
    servo_pin.write(left)
    status_label.config(text="Servo: Kiri (135°)")

def move_right(event=None):
    servo_pin.write(right)
    status_label.config(text="Servo: Kanan (45°)")

def move_center(event=None):
    servo_pin.write(center)
    status_label.config(text="Servo: Tengah (90°)")

# Membuat GUI
root = tk.Tk()
root.title("Kontrol Servo")

# Tombol untuk kontrol
left_button = tk.Button(root, text="← Kiri", command=move_left, width=15, height=2)
left_button.grid(row=0, column=0, padx=10, pady=10)

right_button = tk.Button(root, text="→ Kanan", command=move_right, width=15, height=2)
right_button.grid(row=0, column=1, padx=10, pady=10)

# Label status
status_label = tk.Label(root, text="Servo: Tengah (90°)", font=("Arial", 12))
status_label.grid(row=1, column=0, columnspan=2, pady=10)

# Shortcut keyboard
root.bind('<Left>', move_left)    # Shortcut panah kiri
root.bind('<Right>', move_right)  # Shortcut panah kanan
root.bind('<Up>', move_center)    # Shortcut panah atas untuk kembali ke tengah
root.bind('<Down>', move_center)  # Shortcut panah bawah untuk kembali ke tengah


# Jalankan GUI
try:
    root.mainloop()
except KeyboardInterrupt:
    board.exit()
    root.destroy()

