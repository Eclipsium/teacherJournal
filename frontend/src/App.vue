<template>
    <v-app>
        <v-app-bar
                app
                color="primary"
                dark
                dense
        >
            <v-toolbar-title>Журнал предподавателя</v-toolbar-title>
        </v-app-bar>
        <v-content>
            <HomePage/>
        </v-content>
    </v-app>
</template>

<script>
    import HomePage from './components/homePageComponent';

    export default {
        name: 'App',

        components: {
            HomePage,
        },

        data: () => ({
            //
        }),
    };
</script>
