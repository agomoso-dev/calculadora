import { useState } from 'react';

export function App() {
    const [display, setDisplay] = useState('');

    const handleClick = (value) => {
        setDisplay(display + value);
    };

    const calculateResult = async () => {
        // Si la pantalla está vacía, no hacer nada
        if (!display) return;

        if (display.trim() === '(') {
            alert('Expresión inválida: no se puede calcular un paréntesis solo.');
            return;
        }

        const lastChar = display.trim().slice(-1);
        if (['+', '-', 'x', '/', '.'].includes(lastChar)) {
            alert('Expresión inválida: no puede terminar con un operador.');
            return;
        }

        try {
            const response = await fetch('http://localhost:8000/api/calcular/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ expresion: display })
            });

            const data = await response.json();

            if (response.ok) {
                setDisplay(data.resultado.toString());
            } else {
                alert(data.error || 'Error desconocido del servidor');
            }
        } catch (error) {
            alert('Error de red: No se pudo conectar con el servidor.');
        }
    };

    const clearDisplay = () => {
        setDisplay('');
    };

    const handleDelete = () => {
        setDisplay(display.slice(0, -1));
    };

    const handleRound = () => {
        if (display && !isNaN(display)) {
            setDisplay(Math.round(Number(display)).toString());
        } else {
            alert('Solo se puede redondear un único número.');
        }
    };

    return (
        <div className="calculator-container">
            <div className="calculator">
                <div className="display">{display}</div>
                <div className="buttons">
                    <div className="row">
                        <button onClick={() => handleClick('(')}>(</button>
                        <button onClick={() => handleClick(')')}>)</button>
                        <button onClick={handleRound}>R</button>
                        <button onClick={handleDelete} className="delete-button">DEL</button>
                    </div>
                    <div className="row">
                        <button onClick={() => handleClick('7')}>7</button>
                        <button onClick={() => handleClick('8')}>8</button>
                        <button onClick={() => handleClick('9')}>9</button>
                        <button onClick={() => handleClick('/')} className="operator-button">/</button>
                    </div>
                    <div className="row">
                        <button onClick={() => handleClick('4')}>4</button>
                        <button onClick={() => handleClick('5')}>5</button>
                        <button onClick={() => handleClick('6')}>6</button>
                        <button onClick={() => handleClick('x')} className="operator-button">x</button>
                    </div>
                    <div className="row">
                        <button onClick={() => handleClick('1')}>1</button>
                        <button onClick={() => handleClick('2')}>2</button>
                        <button onClick={() => handleClick('3')}>3</button>
                        <button onClick={() => handleClick('-')} className="operator-button">-</button>
                    </div>
                    <div className="row">
                        <button onClick={() => handleClick('0')}>0</button>
                        <button onClick={() => handleClick('.')}>.</button>
                        <button onClick={calculateResult} className="equal-button">=</button>
                        <button onClick={() => handleClick('+')} className="operator-button">+</button>
                    </div>
                    <div className="row">
                        <button onClick={clearDisplay} className="clear-button">C</button>
                    </div>
                </div>
            </div>
        </div>
    );
}