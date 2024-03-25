
export const fetchContents = async (url, data,method='POST', headers={'content-type': 'application/json'}) => {

    let res = await fetch(url, {
        method: method,
        body: JSON.stringify(data),
        headers: headers,
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