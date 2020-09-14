#!/bin/sh
set -ex

update_index_html()
{
    element_id=${1?}
    element_url=${2?}
    if [ "${element_url}" != "" ]; then
        sed -i "s#id='${element_id}'.*#id='${element_id}' onclick='window.open(\"${element_url}\")'#g" index.html
    fi
    return 0
}

update_ssp_html()
{
    element_id=${1?}
    element_href=${2?}
    if [ "${element_href}" != "" ]; then
        sed -i "s#id='${element_id}'.*#id='${element_id}' href='${element_href}'#g" ssp.html
    fi
    return 0
}

# Main
## Update index.html
for _URL in $(env | grep ODO_)
do
    _KEY=$(echo "${_URL}" | awk -F '=' '{print $1}')
    _VALUE=$(echo "${_URL}" | awk -F '=' '{print $2}')
    update_index_html "${_KEY}" "${_VALUE}"
done

## Update ssp.html
if [ -z "${ODO_SSP_URL}" ]; then
    update_ssp_html ODO_SSP_URL_1 "${ODO_SSP_URL}"
    update_ssp_html ODO_SSP_URL_2 "${ODO_SSP_URL}"
fi

## Start Nginx
nginx -g "daemon off;"
