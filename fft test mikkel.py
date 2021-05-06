import scipy #importerer pakken "scipy"
import scipy.io.wavfile as wavfile #importerer funksjon fra pakken scipy og gir den et nytt navn
import scipy.fftpack as fftpk #importerer funksjoner fra scipy og gir den et nytt navn
from matplotlib import pyplot as plt # importerer funksjoner fra matplotlib og gir den et nytt navn

s_rate, signal = wavfile.read("forskøvet massesenter 30cm_5sek.wav") # leser av .wav filen og lagrer den som "signal"
FFT = abs(fftpk.fft(signal)) #fft på det avleste signalet
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate)) # definerer frekvensområdet som skal vises i plottet/grafen

plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)]) # bestemmer hvilket området plottet skal foregå
s_rate, signal = wavfile.read("base line 30cm_5sek.wav") # leser av .wav filen og lagrer den som "signal"
FFT = abs(fftpk.fft(signal)) #fft på det avleste signalet
freqs = fftpk.fftfreq(len(FFT), (1.0/s_rate)) # definerer frekvensområdet som skal vises i plottet/grafen

plt.plot(freqs[range(len(FFT)//2)], FFT[range(len(FFT)//2)],"red") # bestemmer hvilket området plottet skal foregå
plt.xlabel('Frequency (Hz)') #label x-aksen
plt.ylabel('Amplitude (Ingen benevning)') #label y-aksen
plt.xlim([5, 300])
plt.show() #funksjon som generer plottet