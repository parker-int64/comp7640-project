
export const fetchContents = async (url, data={}, method='POST', headers={'Content-Type':'application/json'}) => {

    let res = await fetch(import.meta.env.DEV ?  `http://127.0.0.1:5000${url}` : url, {
        method: method,
        body: JSON.stringify(data),
        headers: import.meta.env.DEV ? {
            'Content-Type':'application/json',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': "POST,GET,PUT,DELETE",
            'Access-Control-Allow-Credentials': true,
            'Access-Control-Allow-Headers': '*',
            'Access-Control-Max-Age': 3600
        } : headers,
        mode: 'cors',
        redirect: 'follow',
        cache: 'no-cache', 
    }).then((res) => {
        return res.json()
    }).then((json) => {
        return json
    }).catch(err => {
        console.log(err)
    })

    return res
}