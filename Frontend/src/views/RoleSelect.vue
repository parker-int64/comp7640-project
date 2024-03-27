<script setup>
import { NH1,NFlex, NLayout, NDataTable, NCard, NP, NSelect, NButton, NSteps, NStep, NInput, NGrid, NGi, NSpin, NInputNumber, useDialog, NDropdown, useMessage } from 'naive-ui'
import { ref } from 'vue';
import { useVendorDataStore } from '../stores/vendorData'
import { useCustomerDataStore }  from '../stores/customerData'
import { useItemDataStore }  from '../stores/itemData'
import { useRouter } from 'vue-router';

const role = ref(null)
const dialog = useDialog();
const modifyRole = ref(false)  // are we modifying something?
const currentRef = ref(1)     // current step in steps
const currentStatus = ref("process") // by default process

const vendorStore = useVendorDataStore()
const customerStore = useCustomerDataStore()
const itemData = useItemDataStore()

const columns = ref([])
const data = ref([])

const options = ref([
    {
        label: "Customer",
        value: "customer",
    },

    {
        label: "Vendor",
        value: "vendor",
    },

    {
        label: "Admin (You already are)",
        value: "admin",
        disabled: true
    }
])



const updateUserInfo = (value, options) => {
    if( value === 'vendor') {
        role.value = 'vendor'

        vendorStore.getVendorData().then(()=> {
            if(vendorStore.vendorData){
                data.value = vendorStore.vendorData
                console.log(data)
            }

            columns.value = [
                {
                    title: "Vendor ID",
                    key: "vendor_ID"
                },

                {
                    title: "Geographical Presence",
                    key: "geographical_presence"
                },

                {
                    title: "Business Name",
                    key: "business_name"
                },


                {
                    title: "Customer Feedback Score",
                    key: "customer_feedback_score"
                },
            ]
        })

    } else {
        role.value = 'customer'

        customerStore.getCustomerData().then(()=> {
            if(customerStore.customerData){
                data.value = customerStore.customerData
                console.log(data)
            }

            columns.value = [
                {
                    title: "Customer ID",
                    key: "customer_ID"
                },

                {
                    title: "Contact Number",
                    key: "contact_number"
                },

                {
                    title: "Shipping Address",
                    key: "shipping_details"
                },
            ]
        })

    }
}


const inputVendorValues = ref({
    businessName: null,
    geoPresence: null,
    cusFeedback: null,
    orderHis: null,
    passwd: null
})


const inputProductValues = ref({
    productName: null,
    productPrice: null,
    tag1: null,
    tag2: null,
    tag3: null,
    vendorId: null
})



// buttons

const onAddVendorBtn = () => {
    modifyRole.value = true
}

const onBackBtn = () => {
    modifyRole.value = false
}

const onAddProductBtn = () => {
    modifyRole.value = true

    let retOptions = []

    vendorStore.getVendorData().then(() => {
        if ( vendorStore.vendorData ){
            for (const data of vendorStore.vendorData){
                retOptions.push({
                    label: data['business_name'],
                    value: data['vendor_ID']
                })
            }
        }
    })


    if( retOptions ) {
        selectOptions.value = retOptions
    }
}

// handle select values and drop down options
const selectValue = ref(null)
const selectOptions = ref([])


const nextStep = () => {
    if (currentRef.value === null) currentRef.value = 1
    else if (currentRef.value >= 2) currentRef.value = 2
    else currentRef.value++

    if (role.value === 'vendor'){ 
        let newVendor = []
        // validate insert value in db
        for (const key of Object.keys(inputVendorValues.value)) {
            if (inputVendorValues.value[key] === "") {
                inputVendorValues.value[key] = null
            }
            newVendor.push(inputVendorValues.value[key])
        }
    
        vendorStore.addVendor(newVendor).then(() => {
            console.log(vendorStore.addVendorStatus)
    
            if(vendorStore.addVendorStatus.message === 'ok') {
                dialog.success({
                    title: "Message",
                    content: "Success",
                    positiveText: "OK!",
                })
    
                modifyRole.value = false
            } else {
                // fail
                dialog.error({
                    title: "Message",
                    content: `Error ${vendorStore.addVendorStatus.message}`,
                    positiveText: "Dismiss",
                })
    
                currentRef.value = 1

            }        
        })
    } else {
        let newProduct = []

        console.log(inputProductValues.value['vendorId'])

        for (const value of Object.values(inputProductValues.value)) {
            newProduct.push(value)
        }
        
        if ( selectValue.value === null ){

            currentRef.value = 1

            dialog.error({
                title: "Message",
                content: "Error, you must select a vendor",
                positiveText: "Dismiss",
            })
            
        }

        itemData.addItem(newProduct).then(()=> {
            if ( itemData.addItemStatus === 'ok' ){
                dialog.success({
                    title: "Message",
                    content: "Success",
                    positiveText: "OK!",
                })
    
                modifyRole.value = false
            } else {

                currentRef.value = 1

                dialog.error({
                    title: "Message",
                    content: "Error, something went wrong, please check your inputs.",
                    positiveText: "Dismiss",
                })
    
                
            }
        })

    }

}

</script>



<template>

    <n-layout>
        <n-flex style="max-width: 80vw; padding: 0 48px;" align="start" vertical>
            <n-h1>Greetings, administrator!</n-h1>
            <n-card v-if="!modifyRole" bordered style="margin-bottom: 20px;">
                <template #header>
                    <n-flex align="center">
                        <n-p style="margin-bottom: 0;">Please select your role</n-p>
                        <n-select 
                        v-model:value="value" 
                        :options="options" 
                        style="max-width: 300px;" 
                        @update:value="updateUserInfo"/>
                    </n-flex>
                </template>
                <n-data-table
                    :columns="columns"
                    :data="data"
                >

                </n-data-table>

                <n-p v-if=" role === 'vendor' ">{{ `You selected ${role}, you may` }} </n-p>
                <n-p v-else-if="role === 'customer'">{{ `You selected ${role}, you may` }} </n-p>

                <n-button v-if="role === 'vendor' " @click="onAddVendorBtn">Add a vendor</n-button>
                <n-button v-if="role === 'customer' " @click="onAddProductBtn">Add a product</n-button>
            </n-card>


            <n-card v-else style="max-width: 80vw; margin-bottom: 30px" align="start">
                <n-h1 v-if="role === 'vendor' "> {{ 'Add a vendor' }}</n-h1>
                <n-h1 v-if="role === 'customer' "> {{ 'Add a product' }}</n-h1>
                <n-flex justify="end" align="center">
                    <n-steps :current="currentRef" :status="currentStatus">
                        <n-step
                            title="Input"
                            description="Please input your values"
                        />
                        <n-step
                            title="Validate"
                            description="Database validation"
                        />
                    </n-steps>

                    <n-grid v-if="role === 'vendor'"
                        :x-gap="2" 
                        :y-gap="12" 
                        cols="1 s:2 m:2 l:2 xl:2 2xl:2" 
                        responsive="screen"
                        style="max-width: 70vw; margin-top: 50px; align-items: center"
                    >
                        <n-gi span="12">
                            <n-p>Vendor Id will be assigned automatically.</n-p>
                        </n-gi>
                        <n-gi>
                            <n-flex align="center">
                                <n-p>Vendor Business Name</n-p>
                            </n-flex>
                        </n-gi>
                        <n-gi>
                            <n-input v-model:value="inputVendorValues.businessName" type="text" placeholder="Input" />
                        </n-gi>
                        <n-gi>
                            <n-p>Vendor Geographical Presence</n-p>
                        </n-gi>
                        <n-gi>
                            <n-input v-model:value="inputVendorValues.geoPresence" type="text" placeholder="Input" />
                        </n-gi>

                        <n-gi>
                            <n-p>Customer Feedback Score (Optional)</n-p>
                        </n-gi>
                        <n-gi>
                            <n-input-number v-model:value="inputVendorValues.cusFeedback" :step="0.5" :min="0" :max="5"/>
                        </n-gi>

                        <n-gi>
                            <n-p>Order History (Optional)</n-p>
                        </n-gi>
                        <n-gi>
                            <n-input v-model:value="inputVendorValues.orderHis" type="text" placeholder="Input" />
                        </n-gi>

                        <n-gi>
                            <n-p>Password (Optional)</n-p>
                        </n-gi>
                        <n-gi>
                            <n-input v-model:value="inputVendorValues.passwd" type="text" placeholder="Input" />
                        </n-gi>
                    </n-grid>


                    <n-grid v-if="role === 'customer'"
                        :x-gap="2" 
                        :y-gap="12" 
                        cols="1 s:2 m:2 l:2 xl:2 2xl:2" 
                        responsive="screen"
                        style="max-width: 70vw; margin-top: 50px; align-items: center"
                    >
                        <n-gi span="12">
                            <n-p>Product ID will be assigned automatically.</n-p>
                        </n-gi>
                        <n-gi>
                            <n-flex align="center">
                                <n-p>Product Name</n-p>
                            </n-flex>
                        </n-gi>
                        <n-gi>
                            <n-input v-model:value="inputProductValues.productName" type="text" placeholder="Input" />
                        </n-gi>
                        <n-gi>
                            <n-p>Product Price (¥)</n-p>
                        </n-gi>
                        <n-gi>
                            <n-input-number v-model:value="inputProductValues.productPrice" :step="100" :min="0" :max="65535"/>
                        </n-gi>

                        <n-gi>
                            <n-p>Product Tags</n-p>
                        </n-gi>
                        <n-gi>
                            <n-flex justify="center" align="center" style="flex-wrap: nowrap;">
                                <n-input v-model:value="inputProductValues.tag1" type="text" placeholder="Input" />
                                <n-input v-model:value="inputProductValues.tag2" type="text" placeholder="Input" />
                                <n-input v-model:value="inputProductValues.tag3" type="text" placeholder="Input" />
                            </n-flex>
                        </n-gi>

                        <n-gi>
                            <n-p>Vendor Information</n-p>
                        </n-gi>

                        <n-gi>
                            <n-flex align="center" >

                                <n-select trigger="hover" v-model:value="selectValue" :options="selectOptions" />

                            </n-flex>
                        </n-gi>
                    </n-grid>
                    
                    <n-p v-if="role === 'customer'" style="margin: 0">{{ ` (Vendor ID:${selectValue})`  }}  </n-p>

                </n-flex>
                <n-flex justify="center" style="margin-top: 30px;">
                    <n-button @click="onBackBtn">Back</n-button>
                    <n-button type="primary" @click="nextStep">Next</n-button>
                </n-flex>
            </n-card>
        </n-flex>
    </n-layout>

</template>


<style scoped>


</style>