import {ref} from 'vue';
import JSONStream from './JSONStream'

export function fetchData(url, data = {}) {
    const isDone = ref(false);
    const fetchResult = ref([]);
    const jsonStream = new JSONStream({async: false});
    fetch(import.meta.env.VITE_APP_BASE_URL + url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
        .then(response => {
            const reader = response.body.getReader();
            return new ReadableStream({
                start(controller) {
                    function push() {
                        reader.read().then(({done, value}) => {
                            if (done) {
                                controller.close();
                                isDone.value = true;
                                return;
                            }
                            const decoder = new TextDecoder('utf-8');
                            const resonseStr = decoder.decode(value);
                            try {
                                const jsonObj = JSON.parse(resonseStr);
                                fetchResult.value.push(jsonObj);
                            } catch {
                                try {
                                    jsonStream.transform(resonseStr, (error, jsonObj) => {
                                        if (error) {
                                            console.error(error);
                                        } else {
                                            fetchResult.value.push(jsonObj);
                                        }
                                    });
                                } catch (e) {
                                    console.log(e);
                                }
                            }
                            controller.enqueue(value);
                            push();
                        });
                    }

                    push();
                }
            });
        })

    return {isDone, fetchResult};
}

