a
    >��_t  �                   @   sr  d dl mZ d dlmZmZmZ d dlm	Z	 d dl
mZmZ d dlmZ d dlmZ e	d�rded� d d	lmZmZ d
ZdZeee� dZdd� Zedkr�ed� e�  edk�rNe	d�r�e	d�r�edd�Zedd�Ze�� Ze�� Ze� �  e� �  nVe!d�Ze!d�Zedd�Zedd�Ze�"e� e�"e� e� �  e� �  ed� e�  dd� Z#dd� Z$edk�rne$�  dS )�    )�system)�stdout�argv�exit)�exists)�uniform�randint)�sleep)�dateZadvmrz8

		[1;31;40mFirstly install tool  [ sh install.sh ]


)�get�postu�   

÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷


u^   
	± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± ± 

z/-\|c                  C   s8   d} d}t d|  � t d| � td� t d|  � d S )Nz_ '
############################################################################
	 ' | lolcat
	 a#   '
 	_|      _|  _|_|_|                        _|
 	_|_|  _|_|  _|    _|        _|_|_|    _|_|_|  _|      _|
 	_|  _|  _|  _|_|_|        _|    _|  _|    _|  _|      _|
 	_|      _|  _|    _|      _|    _|  _|    _|    _|  _|
 	_|      _|  _|    _|        _|_|_|    _|_|_|      _|
	' | lolcatZechouF   [1;30;40m 	 © script  by  cyco      [  https://github.com/sl-cyco  ])�shell�print)Zname_bar�name� r   �advmr.py�banner   s    r   �__main__�clear�url�auth�rz

enter Url : z
enter Authorization : �wc                  C   sX   dd� } dd� }t | � �dks,t |� �dkr0dS t | � �dksLt |� �dkrPd	S d
S d S )Nc                  S   s    t ddddd�} td| d�}|S )N�
2018.3.0f2�megarun.dialog.lk�
Keep-Alive�gzip��Authorization�X-Unity-Version�Host�
Connection�Accept-Encodingz2https://megarun.dialog.lk/api/v2/reviev/drawpoints�Zheaders)r   r   ��header�resr   r   r   �
drawpointsE   s    zblock_check.<locals>.drawpointsc                  S   s"   t dddddd�} td| d�}|S )	Nr   z!application/x-www-form-urlencodedr   r   r   )r   r   zContent-Typer    r!   r"   z%https://megarun.dialog.lk/api/v2/playr#   )r   r   r$   r   r   r   �playK   s    zblock_check.<locals>.playz<Response [406]>z<Response [201]>z
no blocked�<Response [401]>�blockedZwrong)�str)r'   r(   r   r   r   �block_checkC   s    r,   c                  C   sL  zt � dkrtd� W n   td� Y n0 td�rhtdd�} | �� }| ��  |tt�� �kr�t	d� n(tdd�} | �
tt�� �� | ��  d}d	}d	}d	}d	}d	}d	}d	}d	}	td
dddd�}
d	}td�r�tdd�}|D ]}|�� r�|t|�7 }q�|��  || | | dk�rtd� �qH|tt�� �k�rF|dk�rFtd� �qHtdd�}td� td�D ]8}ttt��D ]$}t|d � t�
dt|  � �qp�q`t	d� t�  tt|
d�}|d7 }t|�dk�r�|d7 }n�t|�dk�r�|jdk�r |d7 }|d7 }nd|jd k�r|d!7 }|d7 }nF|jd"k�r<|d7 }|d7 }n(|jd#k�rZ|d$7 }|d7 }n
t|j� tdd%�}|�
d&� |��  n0t|�d'k�s�|jd(k�r�td)� �qHn|	d7 }	td*ttd+d,�� d- t � td.t|� � td/ttd+d,�� d- t � td0t|� � |	d	k�rXtd/ttd+d,�� d- t � td1ttd+d,�� d2 t|	� � |d	k�r�td/ttd+d,�� d- t � td1ttd+d,�� d3 t|� � |d	k�r�td/ttd+d,�� d- t � td1ttd+d,�� d4 t|� � |d	k�r6td/ttd+d,�� d- t � td1ttd+d,�� d5 t|� � |d	k�r�td/ttd+d,�� d- t � td1ttd+d,�� d6 t|� � || | | d	k�r(td/ttd+d,�� d- t � td1ttd+d,�� d7 t|| | | � � td/ttd+d,�� d- t � td1ttd+d,�� d8 t|
 � d9 � td/ttd+d,�� d- t � q�d S ):Nr*   z'

[1;31;40m [#] ...user blocked... [#]u'   
[0;31;40m[¿] ...no internet... [?]

Ztdyr   zrm tdy mg_countr   z0.0r   r   r   r   r   r   Zmg_count�   z*
[1;36;40m Daily message limit reached...z,
[0;36;40m Daily message limit reached...

�F   �   �
�d   i�  zrunning... r   r#   �   z<Response [204]>z<Response [200]>z{"type":"data","size":10}�
   z{"type":"data","size":50}�2   z{"type":"data","size":100}z{"type":"data","size":200}��   �az1
r)   z.{"status":429,"message":"Rate limit exceeded"}z&
[1;31;40m [#] ...user blocked... [#]z

[0;�    �%   z;40mz	All requests 			: z[0;z	No data responses 		: z[1;z;40m	Wrong requests 			: z;40m	10mb messages 			: z;40m	50mb messages 			: z;40m	100mb messages 			: z;40m	200mb messages 			: z;40m	Total messages 			: z ;40m	Total from this session 	: Zmb)r,   �prnt_extr   �open�read�closer+   r
   Ztodayr   �writer   �	isnumeric�intr   r   �range�len�br	   r   r   r   r   �textr   �bar�cut)Ztdy_contentZdayZall_reqZd10Zd50Zd100Zd200Zttl_dtZno_dtZwrng_reqr%   Zmg_cntZmg_cnt_contentZmgZrnd_time�i�or&   r   r   r   �main\   s�    















"
"
"
"
".(rH   N)%�osr   r   �sysr   r   r   r9   �os.pathr   Zrandomr   r   �timer	   Zdatetimer
   Zrequestsr   r   rD   rE   r   rB   r   �__name__r:   Zurl_contentZauth_contentr;   r   r   r<   �inputr=   r,   rH   r   r   r   r   �<module>   sH   








t
