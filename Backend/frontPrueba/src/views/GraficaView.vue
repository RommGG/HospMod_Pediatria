<template>
    <div>

        <div class="row">
            <div class="column">
                <canvas id="partoNaturalChart" width="400" height="400"></canvas>
            </div>
            <div class="column">
                <canvas id="cesareaChart" width="400" height="400"></canvas>
            </div>
        </div>

    </div>
</template>

<script>
import Chart from 'chart.js/auto';

export default {
    data() {
        return {
            partoNaturalChart: null,
            cesareaChart: null,
            currentData: {
                pnMasculino: null,
                pnFemenino: null,
                cMasculino: null,
                cFemenino: null,
            },
            data: {
                labels: [],
                datasets: [{
                    label: 'Parto Natural',
                    data: [],
                    backgroundColor: ['skyblue', 'lightpink']
                },
                {
                    label: 'Cesárea',
                    data: [],
                    backgroundColor: ['skyblue', 'lightpink']
                }]
            }
        };
    },
    mounted() {
        this.CargarAPI();
        // Inicia el polling para actualizar los datos cada 5 segundos
        setInterval(this.CargarAPI, 3000);
    },
    methods: {
        CargarAPI() {
            /*ruta del endpoint con la vista de mysql, se espera una respuesta*/
            fetch('http://127.0.0.1:8000/hospital/api/partos/')
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Error al Recuperar Los datos');
                    }
                    return response.json();
                })
                .then(data => {
                    // declaracion de las variables que contienen los datos necesario para la grafica
                    const newPnMasculino = data[0].pn_masculino;
                    const newPnFemenino = data[0].pn_femeninos;
                    const newCMasculino = data[0].c_masculino;
                    const newCFemenino = data[0].c_femenino;
                    // Compara los datos nuevos con los actuales 
                    if (this.currentData.pnMasculino !== newPnMasculino ||this.currentData.pnFemenino !== newPnFemenino ||this.currentData.cMasculino !== newCMasculino ||this.currentData.cFemenino !== newCFemenino) {
                        // si la condicion es verdadera se actualizan los datos actuales en la grafica
                        this.currentData.pnMasculino = newPnMasculino;
                        this.currentData.pnFemenino = newPnFemenino;
                        this.currentData.cMasculino = newCMasculino;
                        this.currentData.cFemenino = newCFemenino;
                        // se Llama a la función ActualizarDatos solo si hay cambios, para actualizar la tabla
                        this.ActualizarDatos(newPnMasculino, newPnFemenino, newCMasculino, newCFemenino);
                    }
                })
                .catch(error => {
                    console.error('Error al cargar los datos desde la API:', error);
                });
        },

        /*Escript que se encarga de cargar los datos a las graficas*/
        ActualizarDatos(pnMasculino, pnFemenino, cMasculino, cFemenino) {
            let delayed;
            const data = this.data;
            if (this.partoNaturalChart) {
                this.partoNaturalChart.destroy();
            }
            if (this.cesareaChart) {
                /*Actualiza los datos si han sufrido un cambio*/
                this.cesareaChart.destroy();
            }
            const ctxPartoNatural = document.getElementById('partoNaturalChart').getContext('2d');
            this.partoNaturalChart = new Chart(ctxPartoNatural, {
                type: 'pie',
                data: {
                    labels: ['Masculino', 'Femenino'],
                    datasets: [{
                        label: data.datasets[0].label,
                        data: [pnMasculino, pnFemenino],
                        backgroundColor: data.datasets[0].backgroundColor
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Comparación en Parto Natural'
                        },
                        tooltips: {
                            enabled: false
                        }
                    },

                    animation: {
                        onComplete: () => {
                            delayed = true;
                        },
                        delay: (context) => {
                            let delay = 0;
                            if (context.type === 'data' && context.mode === 'default' && !delayed) {
                                delay = context.dataIndex * 300 + context.datasetIndex * 100;
                            }
                            return delay;
                        },
                    },
                    scales: {
                        x: {
                            stacked: true,
                        },
                        y: {
                            stacked: true
                        }
                    }


                }
            });
        
            const ctxCesarea = document.getElementById('cesareaChart').getContext('2d');
            this.cesareaChart = new Chart(ctxCesarea, {
                type: 'pie',
                data: {
                    labels: ['Masculino', 'Femenino'],
                    datasets: [{
                        label: data.datasets[1].label,
                        data: [cMasculino, cFemenino],
                        backgroundColor: data.datasets[1].backgroundColor
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        title: {
                            display: true,
                            text: 'Comparación en Parto por Cesárea'
                        },
                        tooltips: {
                            enabled: false
                        }
                    },
                    animation: {
                        onComplete: () => {
                            delayed = true;
                        },
                        delay: (context) => {
                            let delay = 0;
                            if (context.type === 'data' && context.mode === 'default' && !delayed) {
                                delay = context.dataIndex * 300 + context.datasetIndex * 100;
                            }
                            return delay;
                        },
                    },
                    scales: {
                        x: {
                            stacked: true,
                        },
                        y: {
                            stacked: true
                        }
                    }
                }
            });
        }
    }
};
</script>

<style scoped>
.row {
    display: flex;
    flex-wrap: wrap;
    /* Permite que las columnas se envuelvan en una fila cuando no hay suficiente espacio */
}

.column {
    flex-basis: 25%;
    /* Cada columna ocupa inicialmente el 25% del ancho */
    padding: 10px;
    /* Añade algo de espacio entre las columnas */
    box-sizing: border-box;
    /* Incluye el padding y el border en el tamaño total de la columna */
    border: 1px solid #ccc;
}

/* Media query para cuando el ancho de la pantalla sea menor o igual a 600px */
@media screen and (max-width: 600px) {
    .column {
        flex-basis: 100%;
        /* Hace que cada columna ocupe todo el ancho disponible */
    }
}
</style>
